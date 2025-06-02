#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct grade
{
    int number;
    char name[10];
    int math;
    int phy;
    int eng;
    int total;
};

int main()
{
    struct grade student[30];
    printf("请将要导入的文件命名为'add.dat',按任意键开始导入\n");
    system("pause");
    FILE *fp1 , *fp2;
    if (fp1 = fopen("add.dat","rb") == NULL)
        printf("文件打开失败\n");
    else
    {
        fp1 = fopen("add.dat","rb");
        int i ,j;
        for(j=0;!feof(fp1);j++)
        {
            fscanf(fp1,"%d  %s  %d  %d  %d  %d",&student[j].number,student[j].name,&student[j].math,&student[j].phy,&student[j].eng,&student[j].total);
        }
        fclose(fp1);
        //printf("导入系统成功\n");
        fp2 = fopen("stu.dat","a");
        for(i=0;i<j;i++)
        {
            fprintf(fp2,"\n%d  %s  %d  %d  %d  %d",student[i].number,student[i].name,student[i].math,student[i].phy,student[i].eng,student[i].total);
        }  
        fclose(fp2);
        printf("成绩导入成功\n");
    }
    system("pause");
    return 0;
}















