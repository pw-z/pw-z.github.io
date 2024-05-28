package pwz.wiki.service.impl;

import org.omg.CORBA.PRIVATE_MEMBER;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pwz.wiki.dao.GuitarDao;
import pwz.wiki.domain.Guitar;
import pwz.wiki.service.GuitarService;

import java.util.List;

@Service
public class GuitarServiceImpl implements GuitarService {

    @Autowired
    private GuitarDao guitarDao;

    public boolean save(Guitar guitar) {
        guitarDao.save(guitar);
        return true;
    }

    public boolean update(Guitar guitar) {
        guitarDao.update(guitar);
        return true;
    }

    public boolean delete(Integer id) {
        guitarDao.delete(id);
        return true;
    }

    public Guitar getById(Integer id) {
        return guitarDao.getById(id);
    }

    public List<Guitar> getAll() {
        return guitarDao.getAll();
    }
}
