package pwz.wiki.service;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import pwz.wiki.domain.Guitar;

import java.util.List;

public interface GuitarService {

    /**
     * 新增吉他
     * @param guitar
     * @return
     */
    public boolean save(Guitar guitar);

    /**
     * 更新吉他
     * @param guitar
     * @return
     */
    public boolean update(Guitar guitar);

    /**
     * 根据id删除吉他
     * @param id
     * @return
     */
    public boolean delete(Integer id);

    /**
     * 根据id查询吉他
     * @param id
     * @return
     */
    public Guitar getById(Integer id);

    /**
     * 查询所有吉他
     * @return
     */
    public List<Guitar> getAll();
}
