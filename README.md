Create an API-wrapper to simplify applications using the
`microspeclib` API.

# Next steps

- [x] wrap calls:
    - [x] give default values
- [ ] add docstrings
- [ ] integrate with project `microspec` as package `microspec`
    - [ ] copy `microspec-api/microspec` into `microspec/src`,
        - [ ] update the `setup.py` to include the new
          `microspec/src/micropsec`
        - [ ] test the new `microspec` API works
    - [ ] copy the `microspec-api/docs` into `microspec/doc`
        - [ ] reorganize `microspec/doc` to integrate with
          `micropsec-api/docs`
        - [ ] update the `conf.py` to pick up the new docs
        - [ ] test the Sphinx build still works
            - do this on Linux, not on Windows
      
