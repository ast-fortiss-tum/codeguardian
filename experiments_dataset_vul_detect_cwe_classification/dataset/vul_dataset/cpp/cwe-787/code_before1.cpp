// Source: Row 104 in ./dataset/CVEfixes/Analysis/results/C++/df_c++_cwe_787.xlsx

void Polygon::Insert( sal_uInt16 nPos, const Point& rPt )
{
    ImplMakeUnique();

    if( nPos >= mpImplPolygon->mnPoints )
        nPos = mpImplPolygon->mnPoints;

    mpImplPolygon->ImplSplit( nPos, 1 );
    mpImplPolygon->mpPointAry[ nPos ] = rPt;
}