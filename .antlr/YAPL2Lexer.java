// Generated from /home/luis/Desktop/college/last-semester/compilers/Lab1_compis2/YAPL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YAPL2Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, CLASS=19, ELSE=20, FALSE=21, FI=22, IF=23, IN=24, INHERITS=25, 
		ISVOID=26, LET=27, LOOP=28, POOL=29, THEN=30, WHILE=31, NEW=32, NOT=33, 
		TRUE=34, STRINGS=35, INTEGERS=36, TYPEID=37, OBJECTID=38, ASIGNOPP=39, 
		OPEN_COMMENT=40, CLOSE_COMMENT=41, COMMENT=42, ONE_LINE_COMMENT=43, WHITESPACE=44;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "CLASS", "ELSE", "FALSE", "FI", "IF", "IN", "INHERITS", "ISVOID", 
			"LET", "LOOP", "POOL", "THEN", "WHILE", "NEW", "NOT", "TRUE", "STRINGS", 
			"INTEGERS", "TYPEID", "OBJECTID", "ASIGNOPP", "A", "C", "D", "E", "F", 
			"H", "I", "L", "N", "O", "P", "R", "S", "T", "U", "V", "W", "ESC", "UNICODE", 
			"HEX", "OPEN_COMMENT", "CLOSE_COMMENT", "COMMENT", "ONE_LINE_COMMENT", 
			"WHITESPACE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'{'", "'}'", "'('", "','", "')'", "':'", "'@'", "'.'", 
			"'let'", "'*'", "'/'", "'+'", "'-'", "'~'", "'<'", "'<='", "'='", null, 
			null, "'false'", null, null, null, null, null, null, null, null, null, 
			null, null, null, "'true'", null, null, null, null, "'<-'", "'(*'", "'*)'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, "CLASS", "ELSE", "FALSE", "FI", 
			"IF", "IN", "INHERITS", "ISVOID", "LET", "LOOP", "POOL", "THEN", "WHILE", 
			"NEW", "NOT", "TRUE", "STRINGS", "INTEGERS", "TYPEID", "OBJECTID", "ASIGNOPP", 
			"OPEN_COMMENT", "CLOSE_COMMENT", "COMMENT", "ONE_LINE_COMMENT", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public YAPL2Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "YAPL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2.\u0170\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3"+
		"\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3"+
		"\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3"+
		"\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3"+
		"\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3"+
		"\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3"+
		"\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3"+
		"\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3"+
		"#\3#\3$\3$\3$\7$\u00fe\n$\f$\16$\u0101\13$\3$\3$\3%\6%\u0106\n%\r%\16"+
		"%\u0107\3&\3&\7&\u010c\n&\f&\16&\u010f\13&\3\'\3\'\7\'\u0113\n\'\f\'\16"+
		"\'\u0116\13\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60"+
		"\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67"+
		"\3\67\38\38\39\39\3:\3:\3:\5:\u0140\n:\3;\3;\3;\3;\3;\3;\3<\3<\3=\3=\3"+
		"=\3>\3>\3>\3?\3?\3?\7?\u0153\n?\f?\16?\u0156\13?\3?\3?\3?\3?\3@\3@\3@"+
		"\3@\7@\u0160\n@\f@\16@\u0163\13@\3@\5@\u0166\n@\3@\3@\3A\6A\u016b\nA\r"+
		"A\16A\u016c\3A\3A\3\u0154\2B\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13"+
		"\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61"+
		"\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q\2S\2U\2W\2Y\2[\2"+
		"]\2_\2a\2c\2e\2g\2i\2k\2m\2o\2q\2s\2u\2w\2y*{+},\177-\u0081.\3\2\34\4"+
		"\2$$^^\3\2\62;\3\2C\\\6\2\62;C\\aac|\3\2c|\4\2CCcc\4\2EEee\4\2FFff\4\2"+
		"GGgg\4\2HHhh\4\2JJjj\4\2KKkk\4\2NNnn\4\2PPpp\4\2QQqq\4\2RRrr\4\2TTtt\4"+
		"\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\n\2$$\61\61^^ddhhppttvv\5\2\62"+
		";CHch\3\2\f\f\5\2\13\f\16\17\"\"\2\u0166\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3"+
		"\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2"+
		"\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35"+
		"\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)"+
		"\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2"+
		"\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2"+
		"A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3"+
		"\2\2\2\2O\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081"+
		"\3\2\2\2\3\u0083\3\2\2\2\5\u0085\3\2\2\2\7\u0087\3\2\2\2\t\u0089\3\2\2"+
		"\2\13\u008b\3\2\2\2\r\u008d\3\2\2\2\17\u008f\3\2\2\2\21\u0091\3\2\2\2"+
		"\23\u0093\3\2\2\2\25\u0095\3\2\2\2\27\u0099\3\2\2\2\31\u009b\3\2\2\2\33"+
		"\u009d\3\2\2\2\35\u009f\3\2\2\2\37\u00a1\3\2\2\2!\u00a3\3\2\2\2#\u00a5"+
		"\3\2\2\2%\u00a8\3\2\2\2\'\u00aa\3\2\2\2)\u00b0\3\2\2\2+\u00b5\3\2\2\2"+
		"-\u00bb\3\2\2\2/\u00be\3\2\2\2\61\u00c1\3\2\2\2\63\u00c4\3\2\2\2\65\u00cd"+
		"\3\2\2\2\67\u00d4\3\2\2\29\u00d8\3\2\2\2;\u00dd\3\2\2\2=\u00e2\3\2\2\2"+
		"?\u00e7\3\2\2\2A\u00ed\3\2\2\2C\u00f1\3\2\2\2E\u00f5\3\2\2\2G\u00fa\3"+
		"\2\2\2I\u0105\3\2\2\2K\u0109\3\2\2\2M\u0110\3\2\2\2O\u0117\3\2\2\2Q\u011a"+
		"\3\2\2\2S\u011c\3\2\2\2U\u011e\3\2\2\2W\u0120\3\2\2\2Y\u0122\3\2\2\2["+
		"\u0124\3\2\2\2]\u0126\3\2\2\2_\u0128\3\2\2\2a\u012a\3\2\2\2c\u012c\3\2"+
		"\2\2e\u012e\3\2\2\2g\u0130\3\2\2\2i\u0132\3\2\2\2k\u0134\3\2\2\2m\u0136"+
		"\3\2\2\2o\u0138\3\2\2\2q\u013a\3\2\2\2s\u013c\3\2\2\2u\u0141\3\2\2\2w"+
		"\u0147\3\2\2\2y\u0149\3\2\2\2{\u014c\3\2\2\2}\u014f\3\2\2\2\177\u015b"+
		"\3\2\2\2\u0081\u016a\3\2\2\2\u0083\u0084\7=\2\2\u0084\4\3\2\2\2\u0085"+
		"\u0086\7}\2\2\u0086\6\3\2\2\2\u0087\u0088\7\177\2\2\u0088\b\3\2\2\2\u0089"+
		"\u008a\7*\2\2\u008a\n\3\2\2\2\u008b\u008c\7.\2\2\u008c\f\3\2\2\2\u008d"+
		"\u008e\7+\2\2\u008e\16\3\2\2\2\u008f\u0090\7<\2\2\u0090\20\3\2\2\2\u0091"+
		"\u0092\7B\2\2\u0092\22\3\2\2\2\u0093\u0094\7\60\2\2\u0094\24\3\2\2\2\u0095"+
		"\u0096\7n\2\2\u0096\u0097\7g\2\2\u0097\u0098\7v\2\2\u0098\26\3\2\2\2\u0099"+
		"\u009a\7,\2\2\u009a\30\3\2\2\2\u009b\u009c\7\61\2\2\u009c\32\3\2\2\2\u009d"+
		"\u009e\7-\2\2\u009e\34\3\2\2\2\u009f\u00a0\7/\2\2\u00a0\36\3\2\2\2\u00a1"+
		"\u00a2\7\u0080\2\2\u00a2 \3\2\2\2\u00a3\u00a4\7>\2\2\u00a4\"\3\2\2\2\u00a5"+
		"\u00a6\7>\2\2\u00a6\u00a7\7?\2\2\u00a7$\3\2\2\2\u00a8\u00a9\7?\2\2\u00a9"+
		"&\3\2\2\2\u00aa\u00ab\5S*\2\u00ab\u00ac\5_\60\2\u00ac\u00ad\5Q)\2\u00ad"+
		"\u00ae\5i\65\2\u00ae\u00af\5i\65\2\u00af(\3\2\2\2\u00b0\u00b1\5W,\2\u00b1"+
		"\u00b2\5_\60\2\u00b2\u00b3\5i\65\2\u00b3\u00b4\5W,\2\u00b4*\3\2\2\2\u00b5"+
		"\u00b6\7h\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7u\2\2"+
		"\u00b9\u00ba\7g\2\2\u00ba,\3\2\2\2\u00bb\u00bc\5Y-\2\u00bc\u00bd\5]/\2"+
		"\u00bd.\3\2\2\2\u00be\u00bf\5]/\2\u00bf\u00c0\5Y-\2\u00c0\60\3\2\2\2\u00c1"+
		"\u00c2\5]/\2\u00c2\u00c3\5a\61\2\u00c3\62\3\2\2\2\u00c4\u00c5\5]/\2\u00c5"+
		"\u00c6\5a\61\2\u00c6\u00c7\5[.\2\u00c7\u00c8\5W,\2\u00c8\u00c9\5g\64\2"+
		"\u00c9\u00ca\5]/\2\u00ca\u00cb\5k\66\2\u00cb\u00cc\5i\65\2\u00cc\64\3"+
		"\2\2\2\u00cd\u00ce\5]/\2\u00ce\u00cf\5i\65\2\u00cf\u00d0\5o8\2\u00d0\u00d1"+
		"\5c\62\2\u00d1\u00d2\5]/\2\u00d2\u00d3\5U+\2\u00d3\66\3\2\2\2\u00d4\u00d5"+
		"\5_\60\2\u00d5\u00d6\5W,\2\u00d6\u00d7\5k\66\2\u00d78\3\2\2\2\u00d8\u00d9"+
		"\5_\60\2\u00d9\u00da\5c\62\2\u00da\u00db\5c\62\2\u00db\u00dc\5e\63\2\u00dc"+
		":\3\2\2\2\u00dd\u00de\5e\63\2\u00de\u00df\5c\62\2\u00df\u00e0\5c\62\2"+
		"\u00e0\u00e1\5_\60\2\u00e1<\3\2\2\2\u00e2\u00e3\5k\66\2\u00e3\u00e4\5"+
		"[.\2\u00e4\u00e5\5W,\2\u00e5\u00e6\5a\61\2\u00e6>\3\2\2\2\u00e7\u00e8"+
		"\5q9\2\u00e8\u00e9\5[.\2\u00e9\u00ea\5]/\2\u00ea\u00eb\5_\60\2\u00eb\u00ec"+
		"\5W,\2\u00ec@\3\2\2\2\u00ed\u00ee\5a\61\2\u00ee\u00ef\5W,\2\u00ef\u00f0"+
		"\5q9\2\u00f0B\3\2\2\2\u00f1\u00f2\5a\61\2\u00f2\u00f3\5c\62\2\u00f3\u00f4"+
		"\5k\66\2\u00f4D\3\2\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8"+
		"\7w\2\2\u00f8\u00f9\7g\2\2\u00f9F\3\2\2\2\u00fa\u00ff\7$\2\2\u00fb\u00fe"+
		"\5s:\2\u00fc\u00fe\n\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe"+
		"\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0102\3\2"+
		"\2\2\u0101\u00ff\3\2\2\2\u0102\u0103\7$\2\2\u0103H\3\2\2\2\u0104\u0106"+
		"\t\3\2\2\u0105\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0105\3\2\2\2\u0107"+
		"\u0108\3\2\2\2\u0108J\3\2\2\2\u0109\u010d\t\4\2\2\u010a\u010c\t\5\2\2"+
		"\u010b\u010a\3\2\2\2\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e"+
		"\3\2\2\2\u010eL\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0114\t\6\2\2\u0111"+
		"\u0113\t\5\2\2\u0112\u0111\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0112\3\2"+
		"\2\2\u0114\u0115\3\2\2\2\u0115N\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0118"+
		"\7>\2\2\u0118\u0119\7/\2\2\u0119P\3\2\2\2\u011a\u011b\t\7\2\2\u011bR\3"+
		"\2\2\2\u011c\u011d\t\b\2\2\u011dT\3\2\2\2\u011e\u011f\t\t\2\2\u011fV\3"+
		"\2\2\2\u0120\u0121\t\n\2\2\u0121X\3\2\2\2\u0122\u0123\t\13\2\2\u0123Z"+
		"\3\2\2\2\u0124\u0125\t\f\2\2\u0125\\\3\2\2\2\u0126\u0127\t\r\2\2\u0127"+
		"^\3\2\2\2\u0128\u0129\t\16\2\2\u0129`\3\2\2\2\u012a\u012b\t\17\2\2\u012b"+
		"b\3\2\2\2\u012c\u012d\t\20\2\2\u012dd\3\2\2\2\u012e\u012f\t\21\2\2\u012f"+
		"f\3\2\2\2\u0130\u0131\t\22\2\2\u0131h\3\2\2\2\u0132\u0133\t\23\2\2\u0133"+
		"j\3\2\2\2\u0134\u0135\t\24\2\2\u0135l\3\2\2\2\u0136\u0137\t\25\2\2\u0137"+
		"n\3\2\2\2\u0138\u0139\t\26\2\2\u0139p\3\2\2\2\u013a\u013b\t\27\2\2\u013b"+
		"r\3\2\2\2\u013c\u013f\7^\2\2\u013d\u0140\t\30\2\2\u013e\u0140\5u;\2\u013f"+
		"\u013d\3\2\2\2\u013f\u013e\3\2\2\2\u0140t\3\2\2\2\u0141\u0142\7w\2\2\u0142"+
		"\u0143\5w<\2\u0143\u0144\5w<\2\u0144\u0145\5w<\2\u0145\u0146\5w<\2\u0146"+
		"v\3\2\2\2\u0147\u0148\t\31\2\2\u0148x\3\2\2\2\u0149\u014a\7*\2\2\u014a"+
		"\u014b\7,\2\2\u014bz\3\2\2\2\u014c\u014d\7,\2\2\u014d\u014e\7+\2\2\u014e"+
		"|\3\2\2\2\u014f\u0154\5y=\2\u0150\u0153\5}?\2\u0151\u0153\13\2\2\2\u0152"+
		"\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0155\3\2"+
		"\2\2\u0154\u0152\3\2\2\2\u0155\u0157\3\2\2\2\u0156\u0154\3\2\2\2\u0157"+
		"\u0158\5{>\2\u0158\u0159\3\2\2\2\u0159\u015a\b?\2\2\u015a~\3\2\2\2\u015b"+
		"\u015c\7/\2\2\u015c\u015d\7/\2\2\u015d\u0161\3\2\2\2\u015e\u0160\n\32"+
		"\2\2\u015f\u015e\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2\u0161"+
		"\u0162\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0166\7\f"+
		"\2\2\u0165\u0164\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\3\2\2\2\u0167"+
		"\u0168\b@\2\2\u0168\u0080\3\2\2\2\u0169\u016b\t\33\2\2\u016a\u0169\3\2"+
		"\2\2\u016b\u016c\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d"+
		"\u016e\3\2\2\2\u016e\u016f\bA\2\2\u016f\u0082\3\2\2\2\16\2\u00fd\u00ff"+
		"\u0107\u010d\u0114\u013f\u0152\u0154\u0161\u0165\u016c\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}