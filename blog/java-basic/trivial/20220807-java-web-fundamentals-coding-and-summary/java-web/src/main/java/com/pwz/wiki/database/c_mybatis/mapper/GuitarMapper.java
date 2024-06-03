package com.pwz.wiki.database.c_mybatis.mapper;

import com.pwz.wiki.database.c_mybatis.pojo.Guitar;

import java.util.List;

public interface GuitarMapper {

    List<Guitar> selectAllGuitar();
}
