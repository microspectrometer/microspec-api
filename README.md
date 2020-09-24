Create an API-wrapper to simplify applications using the
`microspeclib` API.

# Next steps

- [x] wrap calls:
    - [x] give default values
- [ ] add docstrings
- [ ] integrate with project `microspec` as package `microspec`
    - [x] copy `microspec-api/microspec` into `microspec/src`,
        - [x] update the `setup.py` to include the new
          `microspec/src/micropsec`: nothing to do,
          `find_packages()` handles this
        - [x] test the new `microspec` API works: yes
    - [ ] temporarily publish the docs using `microspec-api`
        - take this down later after docs are integrated
    - [ ] copy the `microspec-api/docs` into `microspec/doc`
        - [ ] reorganize `microspec/doc` to integrate with
          `micropsec-api/docs`
        - [ ] update the `conf.py` to pick up the new docs
        - [ ] test the Sphinx build still works
            - do this on Linux, not on Windows
      
