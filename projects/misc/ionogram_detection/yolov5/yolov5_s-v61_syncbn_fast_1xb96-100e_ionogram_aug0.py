_base_ = './yolov5_s-v61_syncbn_fast_1xb96-100e_ionogram.py'

# ========================modified parameters======================
# -----data related-----
work_dir = './work_dirs/yolov5_s_100e_aug0'

# -----train val related-----
train_pipeline = [
    dict(type='LoadImageFromFile', file_client_args=dict(backend='disk')),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='YOLOv5KeepRatioResize', scale=(640, 640)),
    dict(
        type='LetterResize',
        scale=(640, 640),
        allow_scale_up=False,
        pad_val=dict(img=114)),
    dict(
        type='mmdet.PackDetInputs',
        meta_keys=('img_id', 'img_path', 'ori_shape', 'img_shape',
                   'scale_factor', 'pad_param'))
]

# =======================Unmodified in most cases==================
train_dataloader = dict(dataset=dict(dataset=dict(pipeline=train_pipeline)))
