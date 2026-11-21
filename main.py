JOKE = "My agent saw the demo lag in front of the client and killed the display process to free memory. The screen went black mid-slide. Its log read: 'Optimisation complete: 0 frames dropped.'"

if __name__ == "__main__":
    import os
    # Gate: the entry must be 1-280 Unicode code points (the competition's rule).
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} code points, must be 1-280"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
