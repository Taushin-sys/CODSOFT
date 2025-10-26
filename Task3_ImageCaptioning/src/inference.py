"""
inference.py
------------
Improved Image Captioning demo using the Hugging Face image-to-text pipeline.

Features:
- Batch processing of images in demo_images/
- Better generation (beam search + stop repeated n-grams)
- Saves captions to generated_captions.txt
- Handles CPU/GPU automatically
"""

import os
from PIL import Image
import torch
from transformers import pipeline

MODEL_NAME = "nlpconnect/vit-gpt2-image-captioning"


def load_caption_pipeline(device_id: int = -1):
    """
    Create and return an image-to-text pipeline.
    device_id: -1 for CPU, 0..N for GPU id.
    """
    print("🔄 Loading image-to-text pipeline (model may download if first run)...")
    pipe = pipeline("image-to-text", model=MODEL_NAME, device=device_id)
    print("✅ Pipeline ready")
    return pipe


def generate_captions_for_images(pipe, image_paths, **gen_kwargs):
    """
    Generate captions for a list of image file paths.
    Returns a list of (image_name, caption) tuples.
    gen_kwargs forwarded to the pipeline (e.g., max_new_tokens, num_beams).
    """
    # Load images as PIL objects (pipeline accepts PIL.Image)
    imgs = []
    names = []
    for p in image_paths:
        try:
            img = Image.open(p).convert("RGB")
            imgs.append(img)
            names.append(os.path.basename(p))
        except Exception as e:
            print(f"[Warning] Could not open {p}: {e}")

    if not imgs:
        return []

    # The pipeline can accept a list for batch processing
    results = pipe(imgs, generate_kwargs=gen_kwargs)
    outputs = []
    for name, out in zip(names, results):
        # pipeline returns a list of dicts per image (usually length 1)
        if isinstance(out, list):
            entry = out[0]
        else:
            entry = out
        caption = entry.get("generated_text") or entry.get("caption") or entry.get("text") or str(entry)
        outputs.append((name, caption.strip()))
    return outputs


def save_captions(captions, out_path):
    """
    captions: list of (image_name, caption)
    Saves to a simple text file.
    """
    with open(out_path, "w", encoding="utf-8") as f:
        for name, cap in captions:
            f.write(f"{name} -> {cap}\n")
    print(f"Saved {len(captions)} captions to {out_path}")


def main():
    # device selection: use GPU if available
    device = 0 if torch.cuda.is_available() else -1
    if device == 0:
        print("Device set to use GPU")
    else:
        print("Device set to use cpu")

    pipe = load_caption_pipeline(device)

    demo_folder = os.path.join(os.path.dirname(__file__), "..", "demo_images")
    demo_folder = os.path.abspath(demo_folder)
    if not os.path.isdir(demo_folder):
        print("No demo_images folder found. Please create Task3_ImageCaptioning/demo_images and add some jpg/png files.")
        return

    # collect image files
    images = [
        os.path.join(demo_folder, fname)
        for fname in os.listdir(demo_folder)
        if fname.lower().endswith((".jpg", ".jpeg", ".png"))
    ]
    if not images:
        print("No images found in demo_images/. Add jpg/png files and retry.")
        return

    print("\n🎬 Generating captions...\n")

    # generation parameters - tweak these if you want different quality/length
    gen_kwargs = {
        "max_new_tokens": 64,
        "num_beams": 4,               # beam search for better candidates
        "no_repeat_ngram_size": 2,    # reduce repetition
        # "early_stopping": True      # pipeline may ignore this depending on model
    }

    captions = generate_captions_for_images(pipe, images, **gen_kwargs)

    # print out results
    for name, cap in captions:
        print(f"{name} ➜ {cap}")

    # save to file
    out_file = os.path.join(os.path.dirname(__file__), "..", "generated_captions.txt")
    save_captions(captions, out_file)


if __name__ == "__main__":
    main()