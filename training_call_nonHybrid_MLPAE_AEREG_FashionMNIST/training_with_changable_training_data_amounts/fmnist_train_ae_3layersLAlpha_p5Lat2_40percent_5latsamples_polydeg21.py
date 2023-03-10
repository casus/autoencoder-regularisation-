import sys
#sys.path.append('/home/ramana44/topological-analysis-of-curved-spaces-and-hybridization-of-autoencoders')
sys.path.append('./autoencoder-regularisation-')

from datasets import  getDataset
import wandb

import os
from models import AE
import torch



import trainNonHybridMLPAE_AEREGwithFMNIST as train_ae
from activations import Sin

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#Directly loading the dataset presaved as torch tensor after randoming the samples
# The dataset consists of 60000 images in the training set and 10000 images in the test set

# Data presaved to manualy experiment with different amounts of training data

trainImagesFMNIST = torch.load('/home/ramana44/topological-analysis-of-curved-spaces-and-hybridization-of-autoencoders-STORAGE_SPACE/FMNIST_RK_coeffs/trainImages.pt').to(device)
#shape: 60000, 1, 32, 32

testImagesFMNIST = torch.load('/home/ramana44/topological-analysis-of-curved-spaces-and-hybridization-of-autoencoders-STORAGE_SPACE/FMNIST_RK_coeffs/testImages.pt').to(device)
#shape: 10000, 1, 32, 32

noChannels = trainImagesFMNIST.shape[1] # single channel
dx =trainImagesFMNIST.shape[2]   # 32 is the image size along x direction
dy = trainImagesFMNIST.shape[3]  # 32 is the image size along y direction

# Setting up the dataset in batches
batch_size = 200
trainImagesInBatches = trainImagesFMNIST.reshape(int(trainImagesFMNIST.shape[0]/batch_size), batch_size, 1, 32,32)
testImagesInBatches = testImagesFMNIST.reshape(int(testImagesFMNIST.shape[0]/batch_size), batch_size, 1, 32,32)

# the below line of code could be used to directly download the dataset 
#train_loader, test_loader, noChannels, dx, dy = getDataset('FashionMNIST', 200, False)

#To load FashionMNIST dataset in a general way, uncomment the line below and then send
# train_loader and test_loader as input instead of trainImagesInBatches and testImagesInBatches and enumerate 
# through it in the file trainNonHybridMLPAE_AEREGwithFMNIST

# TDA : Training data amount
# Give a value for TDA below such that : 0 < TDA < 1

(model, model_reg, loss_arr_reg, loss_arr_reco, loss_arr_base, loss_arr_val_reco, loss_arr_val_base) = train_ae.train(trainImagesInBatches, testImagesInBatches, dx, dy, noChannels, no_epochs=100, TDA=0.4, reco_loss="mse", latent_dim=10, 
          hidden_size=100, no_layers=3, activation = Sin(), lr=0.0001, alpha = 0.5,
          seed = 2342, train_base_model=True, no_samples=5, deg_poly=21,
          reg_nodes_sampling='legendre', no_val_samples = 10, use_guidance = False,
          enable_wandb=False, wandb_project='ae_reg', wandb_entity='ae_reg_team', weight_jac = False)


