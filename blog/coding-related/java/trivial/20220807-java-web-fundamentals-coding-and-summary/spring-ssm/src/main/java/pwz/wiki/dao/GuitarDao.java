package pwz.wiki.dao;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import pwz.wiki.domain.Guitar;

import java.util.List;

public interface GuitarDao {

//    @Insert("insert into guitar values (#{id}, #{brand}, #{type})")
//    @Insert("insert into guitar (id, brand, type) values (#{id}, #{brand}, #{type})")
    @Insert({"insert into guitar values (#{id}, #{brand}, #{type})"})
    public void save(Guitar guitar);

    @Update("update guitar set brand = #{brand}, type = #{type} where id = #{id}")
    public void update(Guitar guitar);

    @Delete("delete from guitar where id = #{id}")
    public void delete(Integer id);

    @Select("select * from GUITAR where id = #{id}")
    public Guitar getById(Integer id);

    @Select("select * from guitar")
    public List<Guitar> getAll();
}
