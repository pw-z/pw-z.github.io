package com.pwz.wiki.database.mybatis.mapper;

import com.pwz.wiki.database.mybatis.pojo.Guitar;

import java.util.List;

public interface GuitarMapper {

    List<Guitar> selectAllGuitar();
}
