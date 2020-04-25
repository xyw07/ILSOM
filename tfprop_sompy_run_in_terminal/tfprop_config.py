"""Initial configuration for SOM on thermofluid properties."""

# **** configuration for SOM
# ---- number of thread for training
n_job = 1

# ---- input data file
fin = 'after_name_df_lable_42776_partial_random.csv'

# ---- define list of input thermophysical properties
# input_tfprop = ['Name',
#     "ML_MELTINGPOINT",
#     "ML_VISCOSITY",
#     "ML_DENSITY",
#     "ML_GLASSTRANSITION",
#     "ML_THERMALDECOMPOSITION",
#     "ML_THERMALCONDUCTIVITY",
#     "ML_ELECTRICALCONDUCTIVITY",
#     "ML_CYTOTOXICITY",
#     "ML_REFRACTIVEINDEX",
#     "ML_HEATCAPACITY",
#     "ML_SURFACETENSION",
#     "ML_CO2CAPACITY"]
input_tfprop = ['Name', # in this test, Name is type
    "ML_VISCOSITY",
    "ML_THERMALCONDUCTIVITY",
    "ML_ELECTRICALCONDUCTIVITY",
    "ML_CO2CAPACITY"]

# ---- alternative column names for thermophysical properties
name_tfprop = None  # do not use alternative name
# name_tfprop = ['molecular weight [kg/kmol]', 'melting point [°C]',
#                'boiling point [°C]', r'density [kg/m$^{3}$]',
#                'viscosity [mPa·s]',
#                'heat capacity [J/(g·K)]', 'vapor pressure [kPa]',
#                'surface tension [mN/m]', 'thermal conductivity [W/(m·K)]']

# ---- size for SOM map
mapsize = (207, 207)

# ---- file name to store trained data (codebook.matrix) as HDF5 format
isOutTrain = True
fout_train = 'test_big_dataset_ace.h5'
#fout_train ='test_smallset.h5'

# ---- clustering analysis by K-means method
isExeKmean = True
isOutKmeans= True
fout_kmeans = 'data_vis_largeset/kmeans.svg'
km_cluster = 9  # number of clusters
km_seed = 555  # seed for random number generator for K-mean clustering

# ---- clustering via potential method
isExePot = False
gauss_alpha = None  # gaussian alpha calculated automatically
# gauss_alpha = 1.0  # gaussian alpha parameter

potfunc_size = (10, 10)  # figure size
isOutPot = False
# save figure of potential surface
fout_pot = 'data_vis_largeset/potental_surface.svg'

# **** configuration for visualization
# ---- plottting matplotlib style file
#      (style file should be located on
#       ~/.config/matplotlib/stylelib/{style name}.mplstyle in case of linux)
plt_style = 'myclassic'

# ---- SOM positioning map
posmap_size = (10, 10)  # figure size

isOutPosmap = False # generate when training commented by xinyuewang
fout_posmap = 'data_vis_largeset/som_position.svg'

# ---- heat map of all thermofluid properties
heatmap_size = (30, 30)  # figure size

heatmap_col_sz = 4  # number of columns in heat map

isExeHtmap = False
isOutHtmap = False
fout_htmap = 'data_vis_largeset/som_heatmap.svg'

# ---- U-matrix of SOM codebook matrix
umatrix_size = (10, 10)  # figure size

isExeUmat = True
isOutUmat = False
fout_umat = 'data_vis_largeset/som_umat.svg'

# **** configuration for analysis
# ---- elbow method
isExeElbow = True
isOutElbow = True
fout_elbow = 'data_vis_largeset/som_elbow_tets_5job_type.svg'

# ---- silhouette method
isExeSil = True
sil_clust_range = (5, 10)  # range for number of clusters in silhouette method

isOutSil = True
fout_sil = 'data_vis_largeset/som_sil_tets_5job_type'
fout_silext = 'svg'

# ---- correlation matrix
isExeCorrMat = True
corrmat_size = (12, 9)  # figure size of correlation matrix

isOutCorrMat = True
fout_corrmat = 'data_vis_largeset/corr_mat_tets_5job_type.svg'
