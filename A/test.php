<?php
echo "<pre>";

// 地图
$letters = [
    [133, -523, -558, 846, -907, -1224, -1346, 787, -411, -1826],
    [-1478, -853, -1401, 341, -26, 759, -444, 174, -1594, -2000],
    [861, -584, 670, 696, 676, -1674, -1737, -1407, -484, 246],
    [133, -1669, -419, -382, -895, 732, -1278, -1802, -527, 862],
    [133, 544, -1943, 563, -380, -1268, 266, -1309, -1946, 85],
    [133, -1631, -168, 741, -211, -1070, -1873, -554, 243, -901],
    [133, 971, -21, -1111, 463, 944, -127, -1414, -1463, -1287],
    [133, -1886, -1159, -73, 555, -426, -190, -1750, -1028, -188],
    [133, -1654, -931, -1100, -433, -1643, -1281, -455, 904, -126],
    [-1494, -632, 243, 90, 993, 322, 32, -388, -225, 952],
];
// 英雄
$people = [
    'mq' => [10000,100],
    'cyj' => [5000,200],
    'ys' => [2000,500],
    'k' => [1000,1000],
    'drj' => [100,2000],
];

$arr = targets($people, $letters);
//var_dump($arr);
good($arr);

//寻找路线的方法
function targets($people, &$letters, $arr = []) {
    if(empty($arr)){
        $arr['people'] = $people; // 记录英雄血量值,攻击值
        $arr['x'] = 0; // 横向坐标
        $arr['y'] = 0; // 纵向坐标
        $arr['xy'] = []; // 走过的坐标路线
    }
    //英雄伤害计算
    $people = [];
    foreach ($arr['people'] as $key => $value){
        //计算英雄血量
        $value[0] += $letters[$arr['y']][$arr['x']];
        if($value[0] > 0)
            $people[$key] = $value;
    }
    $arr['xy'][] = (string)$arr['x'] .','. (string)$arr['y'];
    $arr['people'] = $people;
    //中途 英雄全部死亡
    if(empty($people)) return [];

    $xLen = count($letters[0]); //横向深度
    $yLen = count($letters);    //纵向深度
    //到达终点 返回路线 英雄血量
    if($arr['x']+1 >= $xLen && $arr['y']+1 >= $yLen){
        return [$arr];
    }

    $xArr = $yArr = $arr;
    $end1 = $end2 = [];
    //向右
    if($xArr['x']+1 < $xLen){
        $xArr['x']++; // 横向坐标
        $end1 = targets($people, $letters, $xArr);
    }
    //向下
    if($yArr['y']+1 < $yLen){
        $yArr['y']++; // 纵向坐标
        $end2 = targets($people, $letters, $yArr);
    }
    $end = array_merge($end1, $end2);
    //返回所有能通过的路线
    return $end;
}
// 筛选出最佳路线
function good($arr) {
    $max = 0;
    $route = [];
    foreach ($arr as $value){
        if($value['people']['mq'][0] > $max){
            $max = $value['people']['mq'][0];
            $route = $value;
        }
    }
    echo json_encode($route);
}
