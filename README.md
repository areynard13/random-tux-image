# Random Tux Image

This project automatically changes the Tux image displayed in the README every day.

Highly inspired by @Yougo-rgb and his <a href="https://github.com/Yougo-rgb/random-code-error">random coding error</a>.

## Image of the Day

![Daily Tux](https://raw.githubusercontent.com/areynard13/random-tux-image/tux-assets/img.png)

## How It Works

1. A Python script (`select_tux.py`) picks a random image from the `images` folder.
2. The script copies this image into the `output` folder and renames it to `img.png`.
3. A GitHub Action runs automatically every day at midnight.
4. The action isolates the `output` folder and pushes its content to the dedicated `tux-assets` branch.

## Add this to your README

If you want to display this daily Tux on your own GitHub profile or repository README, just add the following markdown line to your file:

```markdown
![Daily Tux](https://raw.githubusercontent.com/areynard13/random-tux-image/tux-assets/img.png)
```
