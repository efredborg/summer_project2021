path_to_IRIS_l2 = '/mn/stornext/d9/iris/data/level2/2014/05/21/20140521_114758_3820258168'
dir_save = '/uio/hume/student-u16/eefredbo/Documents/iris2_out/'
filename = 'iris2model_20140521_114758_3820258168_raster_t000_multi.sav'


;goto, here

raster_files = file_search(path_to_IRIS_l2+'/*iris_l2*raster*fits')  ; List of IRIS Level2 raster files
mask = fltarr(4, 775,2)
mask[*,400,*] = 1

raster_files = file_search(path_to_IRIS_l2+'/*iris_l2*raster*fits')  ; List of IRIS Level2 raster files
iris2model = iris2(raster_files[0:4],pca=60,level=2,weights_window = [1.,1/6.,1.,1/6.], dir_save = dir_save,  name_save='5_imgs_iris2model.sav')

;here:

;restore, dir_save+filename
end
