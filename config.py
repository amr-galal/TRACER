def getConfig():
  class Args:
    exp_num = 0
    dataset ='DUTS'
    data_path ='data/'

    # Model parameter settings
    arch = '7'
    channels = [24, 40, 112, 320]
    RFB_aggregated_channel = [32, 64, 128]
    frequency_radius = 16
    denoise = 0.93
    gamma = 0.1

    # Training parameter settings
    img_size = 320
    batch_size = 32
    epochs = 100
    lr = 5e-5
    optimizer = 'Adam'
    weight_decay = 1e-4
    criterion = 'API'
    scheduler = 'Reduce'
    aug_ver = 2
    lr_factor = 0.1
    clipping = 2
    patience = 5
    model_path = 'results/'
    seed = 42
    save_map = None

    # Hardware settings
    multi_gpu = False
    num_workers = 4

  cfg = Args()
  print(f"config arch: {cfg.arch}")
  return cfg