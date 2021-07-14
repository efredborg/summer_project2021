path_to_IRIS_l2 = '/mn/stornext/d9/iris/data/level2/2014/05/21/20140521_114758_3820258168'
dir_save = '/uio/hume/student-u16/eefredbo/Documents/iris2_out/'

;filename = 'iris2model_20140521_114758_3820258168_raster_t000_r00000.sav'
;filename = 'iris2model_20140521_114758_3820258168_raster_t000_r00000_mymask_01_01.sav'
filename = 'iris2model_20140521_114758_3820258168_raster_t000_multi.sav'
filename = '5_imgs_iris2model.sav'


restore, dir_save+filename
num_imgs = uint(size(iris2model, /dimensions))
num_imgs = num_imgs[0]

T = fltarr(num_imgs)
unc_T = fltarr(num_imgs)

vlos = fltarr(num_imgs)
unc_vlos = fltarr(num_imgs)

vturb = fltarr(num_imgs)
unc_vturb = fltarr(num_imgs)

n_e = fltarr(num_imgs)
unc_n_e = fltarr(num_imgs)

poi = [0,400] ; pixel of interest [x, y]
tau_ind = 13 ; corresponding to log(tau) = -5


for i=0, num_imgs -1 do begin
  vars = iris2model[i].model
  uncs = iris2model[i].uncertainty

  T[i] = vars[poi[0],poi[1],tau_ind,0]
  unc_T[i] = uncs[poi[0],poi[1],tau_ind,0]

  vlos[i] = vars[poi[0],poi[1],tau_ind,1]
  unc_vlos[i] = uncs[poi[0],poi[1],tau_ind,1]

  vturb[i] = vars[poi[0],poi[1],tau_ind,2]
  unc_vturb[i] = uncs[poi[0],poi[1],tau_ind,2]

  n_e[i] = vars[poi[0],poi[1],tau_ind,3]
  unc_n_e[i] = uncs[poi[0],poi[1],tau_ind,3]

  endfor

end
