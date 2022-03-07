_base_ = ['../chestnihDatasets224.py', '../../_base_/default_runtime.py']

# use different head for multilabel task
model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='ResNet',
        depth=18,
        num_stages=4,
        out_indices=(3, ),
        style='pytorch'),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='MultiLabelLinearClsHead',
        num_classes=14,
        in_channels=512,
        loss=dict(type='CrossEntropyLoss', use_sigmoid=True, loss_weight=1.0))
)

# load model pretrained on imagenet
load_from = 'https://download.openmmlab.com/mmclassification/v0/resnet/resnet18_8xb32_in1k_20210831-fbbb1da6.pth'  # resnet 18

# optimizer
optimizer = dict(
    type='Adam',
    lr=1e-4,
    betas=(0.9, 0.999),
    paramwise_cfg=dict(custom_keys={'.backbone.classifier': dict(lr_mult=10)}))
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(policy='step', step=40, gamma=0.5)
runner = dict(type='EpochBasedRunner', max_epochs=120)
