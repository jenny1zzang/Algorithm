#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* str1, const char* str2) {
    int len = strlen(str1) + strlen(str2);
    char* answer = (char*)malloc(len+1);
    int i = 0, j = 0;
    for (j=0; j<strlen(str1); j++){
        answer[i++] = str1[j];
        answer[i++] = str2[j];
    }
    answer[i] = '\0';
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    return answer;
}