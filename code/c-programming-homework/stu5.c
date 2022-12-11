#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct grade
{
    int number;
    char name[10];
    int score[4];
};

int main()
{
    struct grade student[30];
    FILE *fp = fopen("stu.dat","r");
    int i = 0,I = 0 ,j = 0;
    for(j=0;!feof(fp);j++)
    {
        fscanf(fp,"%d  %s  %d  %d  %d  %d",&student[j].number,student[j].name,&student[j].score[0],&student[j].score[1],&student[j].score[2],&student[j].score[3]);
    }
    fclose(fp);
    j--;
    int judge;
    printf("请输入要查询的方式\n");
    printf("数学：1  物理：2  英语：3  总分：4\n");
    scanf("%d",&judge);
    judge --;
    struct grade temp;
    for (;i < j;i ++)
    {
        for (I = i + 1;I < j;I ++)
        {
            if (student[i].score[judge] <student[I].score[judge])
            {
                temp = student[I];
                student[I] = student[i];
                student[i] = temp;
            }
        }
    }
    switch (judge)
    {
    	case 0 : printf("按照数学成绩排名后的成绩信息如下：\n学号\t姓名\t数学\t物理\t英语\t总分\t\n");break; 
    	case 1 : printf("按照物理成绩排名后的成绩信息如下：\n学号\t姓名\t数学\t物理\t英语\t总分\t\n");break;
		case 2 : printf("按照英语成绩排名后的成绩信息如下：\n学号\t姓名\t数学\t物理\t英语\t总分\t\n");break;
		case 3 : printf("按照总分成绩排名后的成绩信息如下：\n学号\t姓名\t数学\t物理\t英语\t总分\t\n");break; 
    }
    	
    for (i = 0; i < j ;i ++)
    {
        if (i % 10 == 9)
            printf("\n%d\t%s\t%d\t%d\t%d\t%d\n",student[i].number,student[i].name,student[i].score[0],student[i].score[1],student[i].score[2],student[i].score[3]);
        else
            printf("%d\t%s\t%d\t%d\t%d\t%d\n",student[i].number,student[i].name,student[i].score[0],student[i].score[1],student[i].score[2],student[i].score[3]);
    }
    system("pause");
    return 0;
}


















