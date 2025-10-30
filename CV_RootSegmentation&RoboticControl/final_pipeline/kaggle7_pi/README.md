# Root Detection Pipeline

This project detects and measures plant root lengths from images of Petri dishes.

## Pipeline Steps
1. **Preprocessing**: Removes black edges from the input image to isolate the Petri dish.
2. **Root Mask Prediction**: Predicts root masks using a trained U-Net model.
3. **Division into Sections**: Splits the mask into equal-width sections for each plant.
4. **Root Length Calculation**: Measures the primary root length using skeletonization and graph analysis.

## Outputs
- **Masks**: Saved as PNG files in the results folder.
- **CSV File**: Contains root lengths for all plants.

Run the pipeline and inspect the `results_output` folder for outputs.
