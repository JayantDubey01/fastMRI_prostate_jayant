from matplotlib import pyplot as plt
import h5py

from fastmri_prostate.data.mri_data import load_file_T2, save_recon # main_dir.subfolder.file is the import structure

if __name__=="__main__":

    # Takes h5file and returns kspace, calibration data, ismrmrd header, imgrecon(?), image attributes
    # Values are nd-arrays, im_recon specifically is the shape: [num_of_slices,imh,imw]
    h5file = "/datadrive/Jayant_space/workspace/dataset/T2_IDS_Extracts/fastMRI_prostate_T2_IDS_001_020/file_prostate_AXT2_001.h5"
    kspace, calibration_data, hdr, im_recon, atts = load_file_T2(h5file) 
    print("im_recon type: ", type(im_recon))   
    
    # Reads the my recon stack
    myrecon_data = "/datadrive/Jayant_space/workspace/dataset/Recons/reconstructed_image.h5"
    with h5py.File(myrecon_data, "r") as mf:
        print(mf.keys())
        my_image = mf['reconstruction_rss'][:]

    x,w,h = my_image.shape

    # plot 
    for i in range(x):
        plt.figure()
        plt.subplot(121)
        plt.title("my recon")
        plt.imshow(my_image[i],cmap='gray')
        plt.subplot(122)
        plt.title("orignal recon")
        plt.imshow(im_recon[i],cmap='gray')
        plt.show()