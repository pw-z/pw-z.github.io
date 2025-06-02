package pwz.wiki.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import pwz.wiki.domain.Guitar;
import pwz.wiki.service.GuitarService;

import java.util.List;

@RestController
@RequestMapping("/guitar")
public class GuitarController {

    @Autowired
    private GuitarService guitarService;

    @PostMapping
    public boolean save(@RequestBody Guitar guitar) {
        guitarService.save(guitar);
        return true;
    }

    @PutMapping
    public boolean update(@RequestBody Guitar guitar) {
        guitarService.update(guitar);
        return true;
    }

    @DeleteMapping("/{id}")
    public boolean delete(@PathVariable  Integer id) {
        guitarService.delete(id);
        return true;
    }

    @GetMapping("/{id}")
    public Guitar getById(@PathVariable Integer id) {
        return guitarService.getById(id);
    }

    @GetMapping
    public List<Guitar> getAll() {
        return guitarService.getAll();
    }
}
