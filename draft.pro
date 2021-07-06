
data_dir = '/mn/stornext/d9/iris/data/level2/2014/05/21/20140521_114758_3820258168'
files = find_files('iris_l2*raster*fits', data_dir+'*/')
dim_files = size(files)
; for j = 0, dim_files[1]-1 do print, j,' - ',  strmid(files[j], strpos(files[j],'iris_l2'),100)



data_iris = get_info_irisl2(files[10], factor_and_data=1, mgii_only=1)

data = data_iris.factor.DATA_MG_II_K_2796
wl_mgii = data_iris.factor.wl_mg_ii_k_2796
iris_mgii = transpose(data_iris.factor.DATA_MG_II_K_2796, [2,1,0])
; iris_mgii = data_iris.factor.DATA_MG_II_K_2796
end
sel = tvg(iris_mgii)
dim_sel = size(sel)
; print, dim_sel
; help, sel, /str


; viewing the data
obs_mgii = sel.data_xy[50:450,*]
wl_obs = vac2air(wl_mgii[50:450])
mgII_k_pos_k3 = 2795.528
mgII_h_pos_h3 = 2802.704
mgII_uv_triplet_pos23 = 2797.930 + (2797.998 - 2797.930)

for j=0, dim_sel[1]-1 do begin
  plot, wl_obs, obs_mgii[*,j]
  miver, [mgII_k_pos_k3, mgII_h_pos_h3, mgII_uv_triplet_pos23], line=2
  wait, 5
  endfor
end


; loading the iris2 database
dir_sswdb = '/astro/local/opt/solarsoft_db'
wl_db = readfits(dir_sswdb+'/iris/iris2/latest/wl_iris2.v2.0.fits')
prof_mu_db = readfits(dir_sswdb+'/iris/iris2/latest/inv_mu_iris2.v2.0.fits')
model_db = readfits(dir_sswdb+'/iris/iris2/latest/mod_iris2.v2.0.fits')
prof_db = prof_mu_db[0:472,*]
mu_db = prof_mu_db[473,*]

; taking a look at a profile and its corresponding model atmosphere
!p.multi =[0,2,3,0]
j_db = 500
window, xs=700, ys=700
plot, wl_db, prof_db[*,j_db], xtit='Wavelength [AA]', charsize=2, $
pos = [.1,.7,.95,.95], /norm, /dev
miver, [mgII_k_pos_k3, mgII_h_pos_h3, mgII_uv_triplet_pos23]
plot, indgen(10), xstyle=4, ystyle=4, color=0 ; plots nothing
scales = [1e3, 1e5, 1e5, 1]
titles = ['T [kK]', 'vlos [km/s]', 'vturb [km/s]', 'ne [cm^-3]']
ltau   = findgen(39)*.2 - 7.6
for i = 0, 3 do plot, ltau, model_db[i,*,j_db]/scales[i], title=titles[i], xtitle='log(tau)', charsize=2
!p.multi=0


; looking for the closest RP in the iris2 database
; interpolating the iris2 database to the observations
dim_prof_db= size(prof_db)
dim_obs_mgii=size(obs_mgii)
prof_db2obs = dblarr(dim_obs_mgii[1], dim_prof_db[2])
for i = 0, dim_prof_db[2]-1 do prof_db2obs[*, i] = interpol(prof_db[*,i], wl_db, wl_obs)

; Now, let’s look for the closest RP in the iris2 database interpolated to the observation spectral samples:
euc_dist = calc_dist(obs_mgii, prof_db2obs, mio=1)
w = min(transpose(euc_dist), closest, dim=1)
closest = closest mod dim_prof_db[2]
print, closest
; .r
for j = 0, dim_sel[1]-1 do begin
w = min(euc_dist[j,*], closest)
print, j, closest
endfor
; end


; accelerating the look-up process by working in the PCA space
n_pca  = 50
print, 'Using PCA coef: ', n_pca
mypca, transpose(prof_db2obs), eval, evec
project_pca, transpose(prof_db2obs), eval, evec, n_pca, prof_db2obs_pca_pca, prof_db2obs_pca_coef
prof_db2obs_pca_coef = transpose(prof_db2obs_pca_coef)
project_pca, transpose(obs_mgii), eval, evec, n_pca, obs_mgii_pca, obs_mgii_pca_coef
obs_mgii_pca_coef = transpose(obs_mgii_pca_coef)
euc_dist = calc_dist(obs_mgii_pca_coef, prof_db2obs_pca_coef, mio=1)
; .r
for j =0, dim_sel[1]-1 do begin
    w =  min(closest[j,*], aux)
    print, j, aux
    endfor
end
; Vectorized approach (faster)
w = min(transpose(euc_dist), closest_pca, dim=1)
closest_pca = closest_pca mod dim_prof_db[2]
print, closest_pca
print, closest


; plotting the observed data, the closest RP and its corresponding model

window, xs=700, ys=700
cont_level = 1
!p.multi =[0,2,3,0]
scales = [1e3, 1e5, 1e5, 1]
titles = ['T [kK]', 'vlos [km/s]', 'vturb [km/s]', 'ne [cm^-3]']
ltau   = findgen(39)*.2 - 7.6
for j = 0, dim_sel[1]-1 do begin
plot, wl_obs, obs_mgii[*,j]*cont_level, xtit='Wavelength [AA]', $
              charsize=2, pos = [.1,.7,.95,.95], /norm, /dev, line=2, xstyle=1
oplot, wl_obs, prof_db2obs[*,closest[j]]*cont_level
miver, [mgII_k_pos_k3, mgII_h_pos_h3, mgII_uv_triplet_pos23], line=2
plot, indgen(100), xstyle=4, ystyle=4, color=0 ; plots nothing
for i = 0, 3 do plot, ltau, model_db[i,*,closest[j]]/scales[i], $
            title=titles[i], xtitle='log(tau)', charsize=2
wait, 15
endfor
!p.multi=0
end
