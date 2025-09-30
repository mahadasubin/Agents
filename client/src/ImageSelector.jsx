
export default function ImageSelector({ images }) {
  return (
    <div>
      <h2>Select Image</h2>
      {images.map((img, idx) => (
        <img src={img} key={idx} alt="Suggested" style={{ width: 200, margin: 10 }} />
      ))}
    </div>
  );
}