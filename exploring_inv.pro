goto, here
path_to_IRIS_l2 = '/mn/stornext/d9/iris/data/level2/2014/05/21/20140521_114758_3820258168'
dir_save = '/uio/hume/student-u16/eefredbo/Documents/iris2_out/'

mask = fltarr(4, 775)
mask[*,350:450] = 1
; applying the mask makes the inversion go into a loop

raster_files = file_search(path_to_IRIS_l2+'/*iris_l2*raster*fits')  ; List of IRIS Level2 raster files
iris2model = iris2(raster_files[0],pca=60, delta_mu=0.3,level=2, dir_save = dir_save,weights_window = [1.,1/4.,1.,1/6.], my_mask=mask)
print, total(iris2model.chi2[0:3,395:405])
;end
here:
filename = 'iris2model_20140521_114758_3820258168_raster_t000_r00000.sav'
filename = 'iris2model_20140521_114758_3820258168_raster_t000_r00000_mymask_01_01.sav'
restore, dir_save+filename
end
