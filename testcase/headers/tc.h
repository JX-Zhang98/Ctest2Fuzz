# include <stdio.h>
# include <iostream>
# include "def.h"
# include "tc.h"
using namespace std;

typedef  uint16_t VOS_UINT16;

class MyTestCase0 : public testing::Test
{
    protected:
        virtual void SetUp()
        {
            cout << "TestCase event0 : start" << endl;
        }

        virtual void TearDown()
        {
            cout << "TestCase event0 : end" << endl;
        }
};

int add(int a, VOS_INT16 b);

