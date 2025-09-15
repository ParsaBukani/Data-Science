from .train_model import train_detection_model
from .make_prediction import predict_on_test_set, evaluation_on_test_set
from .load_data import get_datasets



def run_detection_model(mode='train'):

    df_train, df_val, df_test = get_datasets(mode='detection')
    
    if mode == 'train':
        print("\n🚀 Starting model training...")
        train_detection_model(df_train, df_val)
    elif mode == 'evaluation':
        print("\n📊 Evaluating model on test set...")
        evaluation_on_test_set(df_test)
    elif mode == 'prediction':
        print("\n🔍 Making predictions on test set...")
        predict_on_test_set(df_test)