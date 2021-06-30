data_dir = my_dir+'/data/'
files = find_files('iris_l2*raster*fits', data_dir+'*/')
dim_files = size(files)
for j = 0, dim_files[1]-1 do print, j,' - ',  strmid(files[j], strpos(files[j],'iris_l2'),100)
end
