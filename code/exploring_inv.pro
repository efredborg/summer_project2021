path_to_IRIS_l2 = '/mn/stornext/d9/iris/data/level2/2014/05/21/20140521_114758_3820258168'
dir_save = '/uio/hume/student-u16/eefredbo/Documents/iris2_out/'
;goto, here

mask = fltarr(4, 775)
mask[*,350:450] = 1

;raster_files = file_search(path_to_IRIS_l2+'/*iris_l2*raster*fits')  ; List of IRIS Level2 raster files
;iris2model = iris2(raster_files[0:1],pca=60,level=2,weights_window = [1.,1/6.,1.,1/6.], dir_save = dir_save, my_mask=mask)
;print, total(iris2model.chi2[0:3,395:405])
;end
;here:
filename = 'iris2model_20140521_114758_3820258168_raster_t000_r00000.sav'
filename = 'iris2model_20140521_114758_3820258168_raster_t000_r00000_mymask_01_01.sav'
filename = 'iris2model_20140521_114758_3820258168_raster_t000_multi.sav'
;filename = '5_imgs_iris2model.sav'

restore, dir_save+filename
end
print, size(iris2model, /dimensions)
for i=0, 1 do begin
  print, total(iris2model[i].chi2[0:3,395:405])
  endfor
print, total(iris2model[0].chi2[0:3,395:405]) +total(iris2model[1].chi2[0:3,395:405])

end
