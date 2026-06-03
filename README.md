# Random Tux Image

A simple GitHub Action that adds a daily-changing Tux image to your README in 1 line.

Highly inspired by @Yougo-rgb and his <a href="https://github.com/Yougo-rgb/random-code-error">random coding error</a>.

## Image of the Day

![Daily Tux](https://raw.githubusercontent.com/areynard13/random-tux-image/tux-assets/img.png)

## Add this to your README

If you want to display this daily Tux on your own GitHub profile or repository README, just add the following markdown line to your file:

```markdown
![Daily Tux](https://raw.githubusercontent.com/areynard13/random-tux-image/tux-assets/img.png)
```

## How It Works

1. A Python script (`select_tux.py`) picks a random image from the `images` folder.
2. The script copies this image into the `output` folder and renames it to `img.png`.
3. A GitHub Action runs automatically every day at midnight.
4. The action isolates the `output` folder and pushes its content to the dedicated `tux-assets` branch.

## Contributing

Do you have a cool Tux image to share? Contributions are welcome! 

1. **Fork** this repository.
2. Add your image (in `.png` format) to the `images` folder.
3. Open a **Pull Request**.

Once merged, your Tux will be added to the daily rotation!

## Example Of Tux Images

| ![TV](/images/0004_tv.png) | ![Beer](/images/0006_beer.png) | ![Restaurant](/images/0005_restaurant.png) |
|---|---|---|
| ![Chef](/images/0009_pizza_chef.png) | ![Painting](/images/0014_painting.png) | ![Ninja](/images/0010_ninja.png) |
| ![Sled](/images/0008_sled.png) | ![Surf](/images/0001_surf.png) | ![Pyramids](/images/0013_pyramids.png) |

## Support

If you like this project, consider giving it a ⭐ on GitHub.

For questions, issues, or suggestions, feel free to open an issue in this repository.
