path_to_IRIS_l2 = '/mn/stornext/d9/iris/data/level2/2014/05/21/20140521_114758_3820258168'
dir_save = '/uio/hume/student-u16/eefredbo/Documents/iris2_out/'
filename = 'iris2model_20140521_114758_3820258168_raster_t000_multi.sav'


goto, here
;filename = 'iris2model_20140521_114758_3820258168_raster_t000_multi.sav'
; restore, filename, /v

raster_files = file_search(path_to_IRIS_l2+'/*iris_l2*raster*fits')  ; List of IRIS Level2 raster files
iris2model = iris2(raster_files[0:4], level=2, pca = 60, delta_mu = 0.2, dir_save = dir_save)

;iris2model = iris2(raster_files[0]) ; Default call: latest |IRIS2| database, considering all RPs (delta_mu=1), level=0, no weights
;iris2model = iris2(raster_files, version_db='v1.0', delta_mu=0.20, level=2)
;iris2model = iris2(raster_files[11], weights=[1.,1/2.,1.,1/3.], level=1)

here:

restore, dir_save+filename

ltau = iris2model[0].ltau

T_RF = readfits(iris2model[0].rf_db_fits[0])
vlos_RF = readfits(iris2model[0].rf_db_fits[1])
vturb_RF = readfits(iris2model[0].rf_db_fits[2])
nne_RF = readfits(iris2model[0].rf_db_fits[3])

T_node = readfits(iris2model[0].nodes_db_fits[0])
vlos_node = readfits(iris2model[0].nodes_db_fits[1])
vturb_node = readfits(iris2model[0].nodes_db_fits[2])
nne_node = readfits(iris2model[0].nodes_db_fits[3])

; Finding the indices corresponding to the LP fitted to each raster image

inds = iris2model.map_index_db[*,400,*] ; finding for the 5 first images and all 4 rasters
dim_inds = size(inds, /dimensions)
print, dim_inds

end
for i=0, dim_inds[0]-1 do begin
  for j=0, dim_inds[1]-1 do begin
    print,'indices: ', i,j
    ;plot_image, reform(T_RF[*,*,uint(inds[i,j])]), /nosquare
    ;plot_image, reform(vlos_RF[*,*,uint(inds[i,j])]), /nosquare
    ;plot_image, reform(vturb_RF[*,*,uint(inds[i,j])]), /nosquare
    plot_image, reform(nne_RF[*,*,uint(inds[i,j])]), /nosquare
    wait, 2

    endfor
  endfor
;print , inds[*,0]
end
