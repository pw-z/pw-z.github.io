package pwz.wiki.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

@Configuration
@ComponentScan("pwz.wiki")
@EnableWebMvc
public class SpringMvcConfig {
}
