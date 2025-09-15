from sklearn.model_selection import train_test_split
from .load_data import load_detection_image_features, load_plate_features
from .import_to_db import save_datasets

def split_data(df):
    print("📊 Splitting dataset into train/val/test...")
    unique_filenames = df['filename'].unique()

    train_files, temp_files = train_test_split(unique_filenames, test_size=0.3, random_state=42)
    val_files, test_files = train_test_split(temp_files, test_size=0.5, random_state=42)

    df_train = df[df['filename'].isin(train_files)].reset_index(drop=True)
    df_val = df[df['filename'].isin(val_files)].reset_index(drop=True)
    df_test = df[df['filename'].isin(test_files)].reset_index(drop=True)

    print(f"✅ Dataset sizes — Train: {len(df_train)}, Val: {len(df_val)}, Test: {len(df_test)}")

    return df_train, df_val, df_test


if __name__ == "__main__":
    df_d = load_detection_image_features()
    df_train, df_val, df_test = split_data(df_d)
    save_datasets(df_train, df_val, df_test, mode='detection')

    df_p = load_plate_features()
    df_train, df_val, df_test = split_data(df_p)
    split_data(df_p)
    save_datasets(df_train, df_val, df_test, mode='plate')

