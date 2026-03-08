import os
import urllib.request
import zipfile

def setup_kitti_dataset():
    """Download and setup KITTI dataset for AI-IMU-DR"""
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, 'data')
    results_dir = os.path.join(base_dir, 'results')
    
    # Create directories
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)
    
    print("Setting up AI-IMU-DR dataset...")
    print(f"Data directory: {data_dir}")
    print(f"Results directory: {results_dir}")
    
    # Download preprocessed KITTI data
    data_url = "https://github.com/user-attachments/files/17930695/data.zip"
    data_zip = os.path.join(base_dir, 'data.zip')
    
    if not os.path.exists(data_zip):
        print("\nDownloading KITTI IMU data (preprocessed)...")
        urllib.request.urlretrieve(data_url, data_zip)
        print("Download complete!")
    
    # Extract data
    print("\nExtracting data...")
    with zipfile.ZipFile(data_zip, 'r') as zip_ref:
        zip_ref.extractall(base_dir)
    print("Extraction complete!")
    
    # Clean up
    os.remove(data_zip)
    print(f"\nDataset setup complete!")
    print(f"Found {len(os.listdir(data_dir))} data files in {data_dir}")

if __name__ == '__main__':
    setup_kitti_dataset()
