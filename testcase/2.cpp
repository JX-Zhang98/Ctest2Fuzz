# include "tc.h"


TEST_F(MyTestCase0, test_Add){
    int targetValue0 = 9527;
    VOS_UINT16 targetValue1 = 9527;
    int res = add(targetValue0, targetValue1);
}


TEST_F(MyTestCase0, test_addadd){
    int targetValue0 = 65536;
    VOS_UINT16 targetValue1 = 65536;
    int res;
    res = add(targetValue0, targetValue1);
}
