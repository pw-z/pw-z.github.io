package pwz.wiki.service;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import pwz.wiki.config.SpringConfig;
import pwz.wiki.domain.Guitar;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = SpringConfig.class)
public class GuitarServiceTest {

    @Autowired
    private GuitarService guitarService;

    @Test
    public void testGetById(){
        Guitar guitar = guitarService.getById(2);
        System.out.println(guitar);
    }
}
