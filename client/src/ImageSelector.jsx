
export default function ImageSelector({ images }) {
  return (
    <div>
        <img src={images} alt="Suggested" style={{ width: 200, margin: 10 }} />
    </div>
  );
}