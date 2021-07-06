data_dir = '/mn/stornext/d9/iris/data/level2/2014/05/21/20140521_114758_3820258168'
files = find_files('iris_l2*raster*fits', data_dir+'*/')
dim_files = size(files)
iris = get_info_irisl2(files[0], factor_and_data=1, mgii_only=1)

iris_mgii = transpose(iris.factor.DATA_MG_II_K_2796, [2,1,0])


end
