# include "tc.h"



TEST_F(MyTestCase0, test_Add){
    int targetValue0 = 9527;
    VOS_UINT16 targetValue1 = 114514;
    int res = add(targetValue0, targetValue1);
}


TEST_F(MyTestCase0, test_addadd){
    int targetValue0 = 114514;
    VOS_UINT16 targetValue1 = 114514;
    int res;
    res = add(targetValue0, targetValue1);
}

int fuck(int a) {
    return 0;
}