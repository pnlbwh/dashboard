![](pnl-bwh-hms.png)


Project dashboard
=================

   * [Summary](#summary)
      * [Given](#given)
      * [Derivatives](#derivatives)
   * [Details itemwise](#details-itemwise)
      * [Given](#given-1)
         * [T1w](#t1w)
         * [T2w](#t2w)
         * [dwi](#dwi)
      * [Derivatives](#derivatives-1)
         * [Xc](#xc)
         * [Eddy](#eddy)
         * [Ukf](#ukf)
   * [Details casewise](#details-casewise)
      * [Given](#given-2)
      * [Derivatives](#derivatives-2)


# Summary

## Given

|       | T1w | T2w | dwi |
|-------|-----|-----|-----|
| count | 3   | 3   | 2   |

## Derivatives

|       | T1w | T2w | dwi |
|-------|-----|-----|-----|
| count | 3   | 3   | 2   |

# Details itemwise

## Given

### T1w
[Table](https://pnlbwh.github.io/dashboard/R_produced.html)

### T2w
[Table](https://pnlbwh.github.io/dashboard/R_produced.html)


### dwi
[Table](https://pnlbwh.github.io/dashboard/R_produced.html)


## Derivatives

### Xc
[Table](https://pnlbwh.github.io/dashboard/R_produced.html)


### Eddy
[Table](https://pnlbwh.github.io/dashboard/R_produced.html)


### Ukf
[Table](https://pnlbwh.github.io/dashboard/R_produced.html)



# Details casewise

## Given

<details><summary>003GNX012</summary>
<p>

```
/home/tb571/Downloads/INTRuST_BIDS/derivatives/luigi-pnlpipe/sub-003GNX007/
├── anat
│   ├── freesurfer
│   │   ├── label
│   │   ├── mri
│   │   ├── scripts
│   │   ├── stats
│   │   ├── surf
│   │   ├── tmp
│   │   ├── touch
│   │   └── trash
│   ├── sub-003GNX021_desc-T1wXcMabs_mask.nii.gz
│   ├── sub-003GNX021_desc-T2wXcMabs_mask.nii.gz
│   ├── sub-003GNX021_desc-Xc_T1w.nii.gz
│   └── sub-003GNX021_desc-Xc_T2w.nii.gz
├── dwi
│   ├── sub-003GNX021_desc-dwiXcEd_bse.nii.gz
│   ├── sub-003GNX021_desc-dwiXcEdEp_bse.nii.gz
│   ├── sub-003GNX021_desc-XcBseBet_mask.nii.gz
│   ├── sub-003GNX021_desc-Xc_dwi.bval
│   ├── sub-003GNX021_desc-Xc_dwi.bvec
│   ├── sub-003GNX021_desc-Xc_dwi.nii.gz
│   ├── sub-003GNX021_desc-XcEd_dwi.bval
│   ├── sub-003GNX021_desc-XcEd_dwi.bvec
│   ├── sub-003GNX021_desc-XcEd_dwi.nii.gz
│   ├── sub-003GNX021_desc-XcEd_dwi_xfms.tgz
│   ├── sub-003GNX021_desc-XcEdEp_dwi.bval
│   ├── sub-003GNX021_desc-XcEdEp_dwi.bvec
│   ├── sub-003GNX021_desc-XcEdEp_dwi_mask.nii.gz
│   └── sub-003GNX021_desc-XcEdEp_dwi.nii.gz
├── fs2dwi
│   ├── eddy_fs2dwi
│   │   ├── b0maskedbrain.nii.gz
│   │   ├── b0masked.nii.gz
│   │   ├── wmparcInBrain.nii.gz
│   │   └── wmparcInDwi.nii.gz
│   └── epi_fs2dwi
│       ├── b0maskedbrain.nii.gz
│       ├── b0masked.nii.gz
│       ├── wmparcInBrain.nii.gz
│       └── wmparcInDwi.nii.gz
└── tracts

15 directories, 26 files
```

</p>
</details>


<details><summary>003GNX007</summary>
<p>

```
/home/tb571/Downloads/INTRuST_BIDS/derivatives/luigi-pnlpipe/sub-003GNX012/
├── anat
│   ├── freesurfer
│   │   ├── label
│   │   ├── mri
│   │   ├── scripts
│   │   ├── stats
│   │   ├── surf
│   │   ├── tmp
│   │   ├── touch
│   │   └── trash
│   ├── sub-003GNX021_desc-T1wXcMabs_mask.nii.gz
│   ├── sub-003GNX021_desc-T2wXcMabs_mask.nii.gz
│   ├── sub-003GNX021_desc-Xc_T1w.nii.gz
│   └── sub-003GNX021_desc-Xc_T2w.nii.gz
├── dwi
│   ├── sub-003GNX021_desc-dwiXcEd_bse.nii.gz
│   ├── sub-003GNX021_desc-dwiXcEdEp_bse.nii.gz
│   ├── sub-003GNX021_desc-XcBseBet_mask.nii.gz
│   ├── sub-003GNX021_desc-Xc_dwi.bval
│   ├── sub-003GNX021_desc-Xc_dwi.bvec
│   ├── sub-003GNX021_desc-Xc_dwi.nii.gz
│   ├── sub-003GNX021_desc-XcEd_dwi.bval
│   ├── sub-003GNX021_desc-XcEd_dwi.bvec
│   ├── sub-003GNX021_desc-XcEd_dwi.nii.gz
│   ├── sub-003GNX021_desc-XcEd_dwi_xfms.tgz
│   ├── sub-003GNX021_desc-XcEdEp_dwi.bval
│   ├── sub-003GNX021_desc-XcEdEp_dwi.bvec
│   ├── sub-003GNX021_desc-XcEdEp_dwi_mask.nii.gz
│   └── sub-003GNX021_desc-XcEdEp_dwi.nii.gz
├── fs2dwi
│   ├── eddy_fs2dwi
│   │   ├── b0maskedbrain.nii.gz
│   │   ├── b0masked.nii.gz
│   │   ├── wmparcInBrain.nii.gz
│   │   └── wmparcInDwi.nii.gz
│   └── epi_fs2dwi
│       ├── b0maskedbrain.nii.gz
│       ├── b0masked.nii.gz
│       ├── wmparcInBrain.nii.gz
│       └── wmparcInDwi.nii.gz
└── tracts

15 directories, 26 files
```

</p>
</details>


<details><summary>003GNX021</summary>
<p>

```
/home/tb571/Downloads/INTRuST_BIDS/derivatives/luigi-pnlpipe/sub-003GNX021/
├── anat
│   ├── freesurfer
│   │   ├── label
│   │   ├── mri
│   │   ├── scripts
│   │   ├── stats
│   │   ├── surf
│   │   ├── tmp
│   │   ├── touch
│   │   └── trash
│   ├── sub-003GNX021_desc-T1wXcMabs_mask.nii.gz
│   ├── sub-003GNX021_desc-T2wXcMabs_mask.nii.gz
│   ├── sub-003GNX021_desc-Xc_T1w.nii.gz
│   └── sub-003GNX021_desc-Xc_T2w.nii.gz
├── dwi
│   ├── sub-003GNX021_desc-dwiXcEd_bse.nii.gz
│   ├── sub-003GNX021_desc-dwiXcEdEp_bse.nii.gz
│   ├── sub-003GNX021_desc-XcBseBet_mask.nii.gz
│   ├── sub-003GNX021_desc-Xc_dwi.bval
│   ├── sub-003GNX021_desc-Xc_dwi.bvec
│   ├── sub-003GNX021_desc-Xc_dwi.nii.gz
│   ├── sub-003GNX021_desc-XcEd_dwi.bval
│   ├── sub-003GNX021_desc-XcEd_dwi.bvec
│   ├── sub-003GNX021_desc-XcEd_dwi.nii.gz
│   ├── sub-003GNX021_desc-XcEd_dwi_xfms.tgz
│   ├── sub-003GNX021_desc-XcEdEp_dwi.bval
│   ├── sub-003GNX021_desc-XcEdEp_dwi.bvec
│   ├── sub-003GNX021_desc-XcEdEp_dwi_mask.nii.gz
│   └── sub-003GNX021_desc-XcEdEp_dwi.nii.gz
├── fs2dwi
│   ├── eddy_fs2dwi
│   │   ├── b0maskedbrain.nii.gz
│   │   ├── b0masked.nii.gz
│   │   ├── wmparcInBrain.nii.gz
│   │   └── wmparcInDwi.nii.gz
│   └── epi_fs2dwi
│       ├── b0maskedbrain.nii.gz
│       ├── b0masked.nii.gz
│       ├── wmparcInBrain.nii.gz
│       └── wmparcInDwi.nii.gz
└── tracts

15 directories, 26 files
```

</p>
</details>

## Derivatives

<details><summary>003GNX007</summary>
<p>

```
/home/tb571/Downloads/INTRuST_BIDS/derivatives/luigi-pnlpipe/sub-003GNX007/
├── anat
│   ├── freesurfer
│   │   ├── label
│   │   ├── mri
│   │   ├── scripts
│   │   ├── stats
│   │   ├── surf
│   │   ├── tmp
│   │   ├── touch
│   │   └── trash
│   ├── sub-003GNX021_desc-T1wXcMabs_mask.nii.gz
│   ├── sub-003GNX021_desc-T2wXcMabs_mask.nii.gz
│   ├── sub-003GNX021_desc-Xc_T1w.nii.gz
│   └── sub-003GNX021_desc-Xc_T2w.nii.gz
├── dwi
│   ├── sub-003GNX021_desc-dwiXcEd_bse.nii.gz
│   ├── sub-003GNX021_desc-dwiXcEdEp_bse.nii.gz
│   ├── sub-003GNX021_desc-XcBseBet_mask.nii.gz
│   ├── sub-003GNX021_desc-Xc_dwi.bval
│   ├── sub-003GNX021_desc-Xc_dwi.bvec
│   ├── sub-003GNX021_desc-Xc_dwi.nii.gz
│   ├── sub-003GNX021_desc-XcEd_dwi.bval
│   ├── sub-003GNX021_desc-XcEd_dwi.bvec
│   ├── sub-003GNX021_desc-XcEd_dwi.nii.gz
│   ├── sub-003GNX021_desc-XcEd_dwi_xfms.tgz
│   ├── sub-003GNX021_desc-XcEdEp_dwi.bval
│   ├── sub-003GNX021_desc-XcEdEp_dwi.bvec
│   ├── sub-003GNX021_desc-XcEdEp_dwi_mask.nii.gz
│   └── sub-003GNX021_desc-XcEdEp_dwi.nii.gz
├── fs2dwi
│   ├── eddy_fs2dwi
│   │   ├── b0maskedbrain.nii.gz
│   │   ├── b0masked.nii.gz
│   │   ├── wmparcInBrain.nii.gz
│   │   └── wmparcInDwi.nii.gz
│   └── epi_fs2dwi
│       ├── b0maskedbrain.nii.gz
│       ├── b0masked.nii.gz
│       ├── wmparcInBrain.nii.gz
│       └── wmparcInDwi.nii.gz
└── tracts

15 directories, 26 files
```

</p>
</details>


<details><summary>003GNX012</summary>
<p>

```
/home/tb571/Downloads/INTRuST_BIDS/derivatives/luigi-pnlpipe/sub-003GNX012/
├── anat
│   ├── freesurfer
│   │   ├── label
│   │   ├── mri
│   │   ├── scripts
│   │   ├── stats
│   │   ├── surf
│   │   ├── tmp
│   │   ├── touch
│   │   └── trash
│   ├── sub-003GNX021_desc-T1wXcMabs_mask.nii.gz
│   ├── sub-003GNX021_desc-T2wXcMabs_mask.nii.gz
│   ├── sub-003GNX021_desc-Xc_T1w.nii.gz
│   └── sub-003GNX021_desc-Xc_T2w.nii.gz
├── dwi
│   ├── sub-003GNX021_desc-dwiXcEd_bse.nii.gz
│   ├── sub-003GNX021_desc-dwiXcEdEp_bse.nii.gz
│   ├── sub-003GNX021_desc-XcBseBet_mask.nii.gz
│   ├── sub-003GNX021_desc-Xc_dwi.bval
│   ├── sub-003GNX021_desc-Xc_dwi.bvec
│   ├── sub-003GNX021_desc-Xc_dwi.nii.gz
│   ├── sub-003GNX021_desc-XcEd_dwi.bval
│   ├── sub-003GNX021_desc-XcEd_dwi.bvec
│   ├── sub-003GNX021_desc-XcEd_dwi.nii.gz
│   ├── sub-003GNX021_desc-XcEd_dwi_xfms.tgz
│   ├── sub-003GNX021_desc-XcEdEp_dwi.bval
│   ├── sub-003GNX021_desc-XcEdEp_dwi.bvec
│   ├── sub-003GNX021_desc-XcEdEp_dwi_mask.nii.gz
│   └── sub-003GNX021_desc-XcEdEp_dwi.nii.gz
├── fs2dwi
│   ├── eddy_fs2dwi
│   │   ├── b0maskedbrain.nii.gz
│   │   ├── b0masked.nii.gz
│   │   ├── wmparcInBrain.nii.gz
│   │   └── wmparcInDwi.nii.gz
│   └── epi_fs2dwi
│       ├── b0maskedbrain.nii.gz
│       ├── b0masked.nii.gz
│       ├── wmparcInBrain.nii.gz
│       └── wmparcInDwi.nii.gz
└── tracts

15 directories, 26 files
```

</p>
</details>


<details><summary>003GNX021</summary>
<p>

```
/home/tb571/Downloads/INTRuST_BIDS/derivatives/luigi-pnlpipe/sub-003GNX021/
├── anat
│   ├── freesurfer
│   │   ├── label
│   │   ├── mri
│   │   ├── scripts
│   │   ├── stats
│   │   ├── surf
│   │   ├── tmp
│   │   ├── touch
│   │   └── trash
│   ├── sub-003GNX021_desc-T1wXcMabs_mask.nii.gz
│   ├── sub-003GNX021_desc-T2wXcMabs_mask.nii.gz
│   ├── sub-003GNX021_desc-Xc_T1w.nii.gz
│   └── sub-003GNX021_desc-Xc_T2w.nii.gz
├── dwi
│   ├── sub-003GNX021_desc-dwiXcEd_bse.nii.gz
│   ├── sub-003GNX021_desc-dwiXcEdEp_bse.nii.gz
│   ├── sub-003GNX021_desc-XcBseBet_mask.nii.gz
│   ├── sub-003GNX021_desc-Xc_dwi.bval
│   ├── sub-003GNX021_desc-Xc_dwi.bvec
│   ├── sub-003GNX021_desc-Xc_dwi.nii.gz
│   ├── sub-003GNX021_desc-XcEd_dwi.bval
│   ├── sub-003GNX021_desc-XcEd_dwi.bvec
│   ├── sub-003GNX021_desc-XcEd_dwi.nii.gz
│   ├── sub-003GNX021_desc-XcEd_dwi_xfms.tgz
│   ├── sub-003GNX021_desc-XcEdEp_dwi.bval
│   ├── sub-003GNX021_desc-XcEdEp_dwi.bvec
│   ├── sub-003GNX021_desc-XcEdEp_dwi_mask.nii.gz
│   └── sub-003GNX021_desc-XcEdEp_dwi.nii.gz
├── fs2dwi
│   ├── eddy_fs2dwi
│   │   ├── b0maskedbrain.nii.gz
│   │   ├── b0masked.nii.gz
│   │   ├── wmparcInBrain.nii.gz
│   │   └── wmparcInDwi.nii.gz
│   └── epi_fs2dwi
│       ├── b0maskedbrain.nii.gz
│       ├── b0masked.nii.gz
│       ├── wmparcInBrain.nii.gz
│       └── wmparcInDwi.nii.gz
└── tracts

15 directories, 26 files
```

</p>
</details>
