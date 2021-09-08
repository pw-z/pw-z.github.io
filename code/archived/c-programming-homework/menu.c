#include<stdio.h>
#include<stdlib.h>

int main()
{
	int action = 100;
    while(action != 0)
    {    
	    printf("|--------------------------------------------|\n");
	    printf("|                学生成绩管理系统            |\n");
	    printf("|--------------------------------------------|\n");
	    printf("|                1---成绩输入                |\n");
	    printf("|                2---成绩修改                |\n");
	    printf("|                3---查询成绩                |\n");
	    printf("|                4---显示成绩                |\n");
	    printf("|                5---统计成绩               |\n");
	    printf("|                6---注销学生                |\n");
	    printf("|                7---成绩导入                |\n");
	    printf("|                0---退出系统                |\n");
	    printf("|--------------------------------------------|\n");
        printf("请输入菜单项数字(0~7):\n");
        scanf("%d",&action);
        switch (action)
        {
            case 1 : system("stu1.exe");break;
            case 2 : system("stu2.exe");break;
            case 3 : system("stu3.exe");break;
            case 4 : system("stu4.exe");break;
            case 5 : system("stu5.exe");break;
            case 6 : system("stu6.exe");break;
            case 7 : system("stu7.exe");break;
            case 0 : printf("over");break;
        }
        system("cls");
    }
    return 0;
}
