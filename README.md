# Filters App

Filters App is a Streamlit-based web application that allows users to upload an image and apply various filters to it. The app provides a user-friendly interface to experiment with different image processing techniques.

## Features

- Upload an image in JPG, JPEG, or PNG format.
- Apply the following filters:
  - Grayscale
  - Brightness adjustment
  - Style filter
  - HDR (High Dynamic Range)
  - Vintage effect
- View the original and filtered images side by side.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the app in your browser (usually at `http://localhost:8501`).
2. Upload an image using the "Upload an image" button.
3. Select a filter from the dropdown menu.
4. Adjust the filter parameters using the sliders (if applicable).
5. View the original and filtered images side by side.

## Dependencies

- Python 3.x
- Streamlit
- OpenCV
- NumPy
- Matplotlib
- Pillow

## File Structure

- `app.py`: Main application file containing the Streamlit app logic.
- `requirements.txt`: List of dependencies required to run the app.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for providing an easy-to-use framework for building web apps.
- [OpenCV](https://opencv.org/) for the image processing functionalities.