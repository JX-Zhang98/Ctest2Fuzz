# include <stdio.h>
# include <iostream>

using namespace std;

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

