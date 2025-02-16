
# K-means Color Palette Generator

This project applies **K-means clustering** to extract optimized color palettes based on predefined themes (e.g., Elegant, Pop, Minimal).

## 🚀 Installation
```sh
git clone https://github.com/your-username/kmeans-color-palette.git
cd kmeans-color-palette
pip install numpy
pip install matplotlib
pip install pandas
pip install scikit-learn

```

## 📌 Usage
### Run the K-means color clustering script
```sh
python kmeans_palette.py --input_image path/to/your/image.jpg --num_colors 3
```

### Upload changes to GitHub using Zsh script
```sh
git add .
git commit -m "Describe your changes"
```
```sh
./upload.zsh
```
### Example
```zh
python kmeans_palette.py --input_image example.jpg --num_colors 3
```
This will process example.jpg and create a palette with 3 colors.

## 📊 Example Output
This script clusters colors into meaningful palettes based on predefined themes. The result is saved and visualized as follows:

![Example Palette]![output-3](https://github.com/user-attachments/assets/67a26d6b-f40d-4c1d-85e4-b229dca5d5b0)


## 📜 License
MIT
