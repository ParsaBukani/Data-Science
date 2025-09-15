from .tools import worth_ocr_model

def run_ocr_model(mode='train'):

    if mode == 'train':
        print("\n🚀 Starting model (ocr worth) training...")
        worth_ocr_model(train_mode=True)

    elif mode == 'test':    
        print("\n🔍 Evaluation on test set (ocr worth) ...")
        worth_ocr_model(train_mode=False)