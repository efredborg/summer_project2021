
data_dir = '/mn/stornext/d9/iris/data/level2/2014/05/21/20140521_114758_3820258168'
files = find_files('iris_l2*raster*fits', data_dir+'*/')
dim_files = size(files)
for j = 0, dim_files[1]-1 do print, j,' - ',  strmid(files[j], strpos(files[j],'iris_l2'),100)


data_iris = get_info_irisl2(files[10], factor_and_data=1, mgii_only=1)
data = data_iris.factor.DATA_MG_II_K_2796
wl_mgii = data_iris.factor.wl_mg_ii_k_2796
iris_mgii = transpose(data_iris.factor.DATA_MG_II_K_2796, [2,1,0])
iris_mgii = data_iris.factor.DATA_MG_II_K_2796
end
sel = tvg(iris_mgii)
dim_sel = size(sel)
print, dim_sel
help, sel, /str

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
