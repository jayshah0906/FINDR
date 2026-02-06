@echo off
echo ============================================
echo ML Component Setup and Training
echo ============================================
echo.

echo Step 1: Installing dependencies...
pip install -r requirements.txt
echo.

echo Step 2: Generating sample data...
python src/generate_sample_data.py
echo.

echo Step 3: Training model...
python src/train.py
echo.

echo Step 4: Testing prediction...
python src/predict.py
echo.

echo ============================================
echo SETUP COMPLETE!
echo ============================================
echo.
echo Model saved to: models/parking_model.pkl
echo Ready for integration with backend!
echo.
pause
