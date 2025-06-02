#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct grade
{
    int number;
    char name[60];
    int math;
    int phy;
    int eng;
    int total;
}student[100];

int main()
{
    FILE *fp = fopen("stu.dat","rb");
    int i ,j;
    for(j=0;!feof(fp);j++)
    {
        fscanf(fp,"%d  %s  %d  %d  %d  %d",&student[j].number,student[j].name,&student[j].math,&student[j].phy,&student[j].eng,&student[j].total);
    }
    fclose(fp);
    

    printf("当前数据库中的学生成绩信息如下：\n学号\t姓名\t数学\t物理\t英语\t总分\t\n");
   for (i = 0; i < j;i ++)
    {
        if (i % 10 == 9)
            printf("%d\t%s\t%d\t%d\t%d\t%d\n\n\n",student[i].number,student[i].name,student[i].math,student[i].phy,student[i].eng,student[i].total);
        else
            printf("%d\t%s\t%d\t%d\t%d\t%d\n",student[i].number,student[i].name,student[i].math,student[i].phy,student[i].eng,student[i].total);
    }
    
    
    system("pause");
    return 0;
}








