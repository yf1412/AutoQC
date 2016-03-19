import qctests.ICDC_aqc_06_n_temperature_extrema as ICDC_nte

import util.testingProfile
import numpy as np

##### ICDC number of temperature extrema.
##### --------------------------------------------------

def test_ICDC_n_temperature_extrema():
    '''Make sure code processes data supplied by Viktor Gouretski
       correctly.
    '''

    lines = data.splitlines()
    for i, line in enumerate(lines):
        if line[0:2] == 'HH':
            header  = line.split()
            nlevels = int(header[-1][:-3])
            
            depths  = []
            temps   = []
            qctruth = []
            for j in range(nlevels):
                d = lines[i + j + 1].split()
                depths.append(float(d[0]))
                temps.append(float(d[1]))
                qctruth.append(int(d[2]) > 0)
            
            p  = util.testingProfile.fakeProfile(temps, depths)
            qc = ICDC_nte.test(p)
       
            assert np.array_equal(qc, qctruth), 'Failed profile with header ' + line

# Data provided by Viktor Gouretski, ICDC, University of Hamburg.
data = '''
HH    6682679   -11.700   -81.433 1968  2 11     21OSD
     .0    25.090 1
    9.0    25.060 1
   10.0    23.780 1
   19.0    24.920 1
   20.0    23.750 1
   28.0    21.440 1
   29.0    23.780 1
   47.0    19.510 1
   49.0    23.780 1
   71.0    17.410 1
   77.0    23.770 1
   94.0    15.650 1
  100.0    23.720 1
  141.0    13.180 1
  145.0    21.930 1
  188.0    12.360 1
  191.0    19.160 1
  328.0    13.220 1
  439.0    10.710 1
  540.0     7.650 1
  640.0     4.650 1
HH    3230656    20.580  -156.100 1967  6 14    378CTD
     .0    26.370 1
    2.0    26.370 1
    4.0    26.370 1
    6.0    26.370 1
    8.0    26.370 1
   10.0    26.360 1
   12.0    26.350 1
   14.0    26.330 1
   16.0    26.240 1
   18.0    26.100 1
   20.0    25.960 1
   22.0    25.820 1
   24.0    25.670 1
   26.0    25.600 1
   28.0    25.580 1
   30.0    25.530 1
   32.0    25.440 1
   34.0    25.310 1
   36.0    25.170 1
   38.0    25.090 1
   40.0    25.060 1
   42.0    25.010 1
   44.0    24.940 1
   46.0    24.870 1
   48.0    24.810 1
   50.0    24.670 1
   52.0    24.390 1
   54.0    24.160 1
   56.0    24.050 1
   58.0    23.930 1
   60.0    23.750 1
   62.0    23.520 1
   64.0    23.320 1
   66.0    23.220 1
   68.0    23.090 1
   70.0    22.860 1
   72.0    22.650 1
   76.0    22.410 1
   78.0    22.220 1
   80.0    22.000 1
   82.0    21.880 1
   84.0    21.790 1
   86.0    21.650 1
   88.0    21.560 1
   90.0    21.460 1
   92.0    21.300 1
   94.0    22.520 1
   96.0    21.090 1
   98.0    21.060 1
  100.0    21.020 1
  102.0    20.970 1
  104.0    20.930 1
  106.0    20.870 1
  108.0    20.770 1
  110.0    20.690 1
  112.0    20.620 1
  114.0    15.960 1
  116.0    20.500 1
  118.0    20.460 1
  120.0    20.410 1
  122.0    20.290 1
  124.0    20.050 1
  126.0    19.770 1
  128.0    19.600 1
  130.0    19.480 1
  132.0    19.380 1
  134.0    20.560 1
  136.0    19.170 1
  138.0    19.090 1
  140.0    18.980 1
  142.0    18.830 1
  144.0    18.700 1
  146.0    18.580 1
  148.0    18.440 1
  150.0    18.250 1
  152.0    18.050 1
  154.0    19.270 1
  156.0    17.770 1
  158.0    17.630 1
  160.0    17.540 1
  162.0    17.490 1
  164.0    17.430 1
  166.0    17.310 1
  168.0    17.210 1
  170.0    17.160 1
  172.0    17.180 1
  174.0    17.900 1
  176.0    17.090 1
  178.0    17.030 1
  180.0    16.980 1
  182.0    16.880 1
  184.0    16.750 1
  186.0    16.620 1
  188.0    16.490 1
  190.0    16.350 1
  192.0    16.180 1
  194.0    17.170 1
  196.0    15.750 1
  198.0    15.610 1
  200.0    15.530 1
  202.0    15.470 1
  204.0    15.400 1
  206.0    15.340 1
  208.0    15.270 1
  210.0    15.190 1
  212.0    15.090 1
  214.0    15.010 1
  216.0    14.910 1
  218.0    14.790 1
  220.0    14.680 1
  222.0    14.550 1
  224.0    14.370 1
  226.0    14.150 1
  228.0    13.990 1
  230.0    13.940 1
  232.0    13.850 1
  234.0    13.650 1
  236.0    13.480 1
  238.0    13.390 1
  240.0    13.350 1
  242.0    13.320 1
  244.0    13.280 1
  246.0    13.210 1
  248.0    13.130 1
  250.0    13.030 1
  252.0    12.910 1
  254.0    12.760 1
  256.0    12.560 1
  258.0    12.270 1
  260.0    11.940 1
  262.0    11.740 1
  264.0    11.660 1
  266.0    11.590 1
  268.0    11.540 1
  270.0    11.500 1
  272.0    11.470 1
  274.0    11.440 1
  276.0    11.420 1
  278.0    11.400 1
  280.0    11.360 1
  282.0    11.290 1
  284.0    11.200 1
  286.0    11.100 1
  288.0    10.980 1
  290.0    10.840 1
  292.0    10.700 1
  294.0    10.580 1
  296.0    10.480 1
  298.0    10.410 1
  300.0    10.350 1
  302.0    10.250 1
  304.0    10.140 1
  306.0    10.070 1
  308.0    10.030 1
  310.0     9.990 1
  312.0     9.960 1
  314.0     9.910 1
  316.0     9.850 1
  318.0     9.780 1
  320.0     9.730 1
  322.0     9.700 1
  324.0     9.670 1
  326.0     9.650 1
  328.0     9.630 1
  330.0     9.610 1
  332.0     9.580 1
  334.0     9.490 1
  336.0     9.340 1
  338.0     9.230 1
  340.0     9.180 1
  342.0     9.150 1
  344.0     9.130 1
  346.0     9.120 1
  348.0     9.090 1
  350.0     9.010 1
  352.0     8.900 1
  354.0     8.770 1
  356.0     8.660 1
  358.0     8.570 1
  360.0     8.510 1
  362.0     8.470 1
  364.0     8.430 1
  366.0     8.370 1
  368.0     8.310 1
  370.0     8.280 1
  372.0     8.300 1
  374.0     8.330 1
  376.0     8.300 1
  378.0     8.260 1
  380.0     8.250 1
  382.0     8.250 1
  384.0     8.250 1
  386.0     8.240 1
  388.0     8.230 1
  390.0     8.220 1
  392.0     8.200 1
  394.0     8.190 1
  396.0     8.190 1
  398.0     8.190 1
  400.0     8.130 1
  402.0     8.000 1
  404.0     7.910 1
  406.0     7.860 1
  408.0     7.820 1
  410.0     7.810 1
  412.0     7.780 1
  414.0     7.710 1
  416.0     7.630 1
  418.0     7.570 1
  420.0     7.540 1
  422.0     7.510 1
  424.0     7.490 1
  426.0     7.460 1
  428.0     7.410 1
  430.0     7.380 1
  432.0     7.350 1
  434.0     7.320 1
  436.0     7.280 1
  438.0     7.240 1
  440.0     7.220 1
  442.0     7.190 1
  444.0     7.170 1
  446.0     7.160 1
  448.0     7.150 1
  450.0     7.100 1
  452.0     7.020 1
  454.0     6.980 1
  456.0     6.970 1
  458.0     6.960 1
  460.0     6.940 1
  462.0     6.900 1
  464.0     6.850 1
  466.0     6.820 1
  468.0     6.820 1
  470.0     6.840 1
  472.0     6.850 1
  474.0     6.830 1
  476.0     6.790 1
  478.0     6.740 1
  480.0     6.690 1
  482.0     6.660 1
  484.0     6.640 1
  486.0     6.610 1
  488.0     6.560 1
  490.0     6.540 1
  492.0     6.530 1
  494.0     6.520 1
  496.0     6.520 1
  498.0     6.530 1
  500.0     6.520 1
  502.0     6.530 1
  504.0     6.530 1
  506.0     6.530 1
  508.0     6.520 1
  510.0     6.520 1
  512.0     6.520 1
  514.0     6.510 1
  516.0     6.490 1
  518.0     6.470 1
  520.0     6.440 1
  522.0     6.410 1
  524.0     6.390 1
  526.0     6.390 1
  528.0     6.390 1
  530.0     6.400 1
  532.0     6.400 1
  534.0     6.400 1
  536.0     6.390 1
  538.0     6.390 1
  540.0     6.390 1
  542.0     6.380 1
  544.0     6.370 1
  546.0     6.360 1
  548.0     6.350 1
  550.0     6.310 1
  552.0     6.260 1
  554.0     6.220 1
  556.0     6.200 1
  558.0     6.170 1
  560.0     6.150 1
  562.0     6.140 1
  564.0     6.120 1
  566.0     6.100 1
  568.0     6.070 1
  570.0     6.060 1
  572.0     6.050 1
  574.0     6.040 1
  576.0     6.030 1
  578.0     6.010 1
  580.0     5.970 1
  582.0     5.940 1
  584.0     5.910 1
  586.0     5.900 1
  588.0     5.900 1
  590.0     5.880 1
  592.0     5.860 1
  594.0     5.850 1
  596.0     5.850 1
  598.0     5.840 1
  600.0     5.820 1
  602.0     5.790 1
  604.0     5.770 1
  606.0     5.760 1
  608.0     5.750 1
  610.0     5.740 1
  612.0     5.730 1
  614.0     5.720 1
  616.0     5.720 1
  618.0     5.710 1
  620.0     5.690 1
  622.0     5.660 1
  624.0     5.620 1
  626.0     5.610 1
  628.0     5.600 1
  630.0     5.590 1
  632.0     5.570 1
  634.0     5.550 1
  636.0     5.540 1
  638.0     5.540 1
  640.0     5.540 1
  642.0     5.530 1
  644.0     5.530 1
  646.0     5.520 1
  648.0     5.510 1
  650.0     5.510 1
  652.0     5.490 1
  654.0     5.470 1
  656.0     5.450 1
  658.0     5.440 1
  660.0     5.420 1
  662.0     5.420 1
  664.0     5.420 1
  666.0     5.400 1
  668.0     5.370 1
  670.0     5.340 1
  672.0     5.330 1
  674.0     5.310 1
  676.0     5.300 1
  678.0     5.300 1
  680.0     5.300 1
  682.0     5.290 1
  684.0     5.280 1
  686.0     5.280 1
  688.0     5.280 1
  690.0     5.270 1
  692.0     5.250 1
  694.0     5.240 1
  696.0     5.220 1
  698.0     5.210 1
  700.0     5.200 1
  702.0     5.190 1
  704.0     5.180 1
  706.0     5.180 1
  708.0     5.180 1
  710.0     5.170 1
  712.0     5.170 1
  714.0     5.150 1
  716.0     5.140 1
  718.0     5.140 1
  720.0     5.150 1
  722.0     5.160 1
  724.0     5.160 1
  726.0     5.160 1
  728.0     5.150 1
  730.0     5.140 1
  732.0     5.130 1
  734.0     5.120 1
  736.0     5.110 1
  738.0     5.100 1
  740.0     5.100 1
  742.0     5.100 1
  744.0     5.090 1
  746.0     5.090 1
  748.0     5.100 1
  750.0     5.100 1
  752.0     5.100 1
  754.0     5.100 1
  756.0     5.100 1
HH   10083172   -17.240   109.580 1996  6 17    103PFL
    5.0    25.147 1
    9.9    25.181 1
   13.9    25.170 1
   18.9    25.170 1
   23.9    25.343 1
   28.8    25.540 1
   33.8    25.528 1
   38.8    25.551 1
   43.7    25.528 1
   48.7    25.540 1
   53.7    25.551 1
   58.6    25.493 1
   63.6    25.250 1
   68.6    24.952 1
   73.5    24.929 1
   78.5    24.182 1
   82.5    25.089 1
   87.5    23.936 1
   92.4    23.306 1
   97.4    22.804 1
  102.4    22.545 1
  107.3    22.096 1
  112.3    22.021 1
  117.3    20.283 1
  122.2    20.652 1
  127.2    22.427 1
  132.2    21.368 1
  137.1    22.470 1
  142.1    22.021 1
  146.1    21.619 1
  151.0    21.883 1
  156.0    22.707 1
  161.0    21.598 1
  165.9    20.704 1
  170.9    20.355 1
  175.9    19.216 1
  180.8    18.603 1
  185.8    18.290 1
  190.8    18.143 1
  195.7    17.746 1
  200.7    17.429 1
  205.7    17.660 1
  210.6    17.564 1
  214.6    17.219 1
  219.6    17.086 1
  224.5    16.641 1
  229.5    16.200 1
  234.5    16.032 1
  239.4    15.864 1
  244.4    15.605 1
  249.4    15.513 1
  254.3    15.393 1
  259.3    14.999 1
  264.2    14.780 1
  269.2    14.644 1
  274.2    14.445 1
  279.1    14.192 1
  286.1    13.861 1
  296.0    13.566 1
  305.9    13.149 1
  314.9    12.683 1
  324.8    12.255 1
  334.7    11.743 1
  344.6    11.304 1
  354.6    11.022 1
  364.5    10.706 1
  374.4    10.477 1
  383.3    10.249 1
  393.3    10.055 1
  403.2     9.903 1
  413.1     9.744 1
  423.0     9.551 1
  432.9     9.342 1
  442.9     9.142 1
  451.8     9.034 1
  461.7     8.934 1
  471.6     8.727 1
  481.5     8.495 1
  491.5     8.265 1
  501.4     8.108 1
  511.3     7.944 1
  520.2     7.846 1
  530.1     7.690 1
  545.0     7.486 1
  564.8     7.233 1
  583.7     7.014 1
  603.5     6.908 1
  623.3     6.803 1
  643.1     6.657 1
  662.0     6.560 1
  681.8     6.447 1
  701.6     6.374 1
  720.4     6.286 1
  740.2     6.181 1
  760.0     6.084 1
  779.8     5.964 1
  798.7     5.867 1
  818.5     5.755 1
  838.3     5.675 1
  857.1     5.603 1
  876.9     5.523 1
  896.7     5.467 1
  916.5     5.411 1
HH   11088555   -68.509   -75.534 2004  4 19     12APB
    4.9      .036 1
   14.8     1.023 1
   32.7    -1.274 1
   54.4     -.987 1
   70.3     1.439 1
   74.2      .759 1
   82.2     -.011 1
  111.8    -1.377 1
  131.6     1.310 1
  200.9     -.389 1
  252.3      .267 1
  416.4     1.299 1
HH    4364914    34.920   -47.920 1950  1  6     27MBT
     .0    19.500 1
    5.0    26.100 1
   10.0    19.400 1
   15.0    34.200 1
   20.0    26.800 1
   25.0    26.200 1
   30.0    26.800 1
   35.0    19.500 1
   40.0    19.100 1
   45.0    19.100 1
   50.0    19.000 1
   55.0    19.000 1
   60.0    19.000 1
   65.0    18.900 1
   70.0    18.900 1
   75.0    18.900 1
   80.0    18.900 1
   85.0    18.900 1
   90.0    18.900 1
   95.0    18.900 1
  100.0    18.900 1
  105.0    18.800 1
  110.0    18.800 1
  115.0    18.800 1
  120.0    18.800 1
  125.0    18.800 1
  130.0    18.800 1
HH    2067338    37.900   -67.130 1968  4  1     20XBT
     .0    19.710 1
    1.0    19.890 1
   28.0    19.050 1
   58.0    16.150 1
   65.0    14.350 1
   69.0    13.760 1
   85.0    12.000 1
   91.0    10.790 1
   96.0     9.640 1
  120.0    10.360 1
  127.0    11.880 1
  144.0    11.360 1
  148.0    12.390 1
  163.0    11.610 1
  196.0    10.860 1
  203.0    12.370 1
  250.0    12.880 1
  283.0    13.010 1
  317.0    11.510 1
  326.0    11.330 1
'''
