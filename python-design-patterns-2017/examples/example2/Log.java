class Log {

    public void writeLog(File f) {
        f.write('Error');
    }

    // Do I really care about the data type? No. Only the interface.
    public void writeLog(IWriter w) {
        w.write('Error');
    }
    // a.k.a. Dependency Injection, IoC
}
